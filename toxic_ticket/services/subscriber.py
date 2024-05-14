import success
import errors
import json
from config.config import get_redis_connection, Settings
from services.utils.redis_message import RedisMessage
from services.user import *
from models.user import User
from tasks.discord_response_queue import *

class ToxicTicket:
    """
    Mirrors the class schema we use in the discord_wrapper microservice.
    """
    def __init__(self, username: str, ticket_type: str, amount: int, issuer: str, channel: str):
        self.username = username
        self.ticket_type = ticket_type
        self.amount = amount
        self.issuer = issuer
        self.channel = channel 

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)


async def process_channel():
    client = await get_redis_connection()
    channel = client.pubsub()
    await channel.subscribe(Settings().TOXIC_TICKET_CHANNEL)
    async for message in channel.listen():
        redis_msg = RedisMessage(message)
        if redis_msg.msgtype != 'subscribe': await process_message(redis_msg.data)

async def check_if_retrieval(message):
    return True if message.get("retrieval") else False

async def process_message(message):
    is_retrieval = await check_if_retrieval(message)
    if is_retrieval:
        await process_retrieval(message)
    else:
        await process_ticket(message)

async def process_retrieval(message):
    username = message.get('username')
    channel = message.get('channel')
    user = await get_user_by_name_service(username)
    if not user:
        await send_error_message_to_server({ 
            "username": username, 
            "channel": channel,
            "action": "missing_user"
        })
    else:
        await send_user_to_server(user, channel)

async def process_ticket(message):
    task = ToxicTicket(**message)
    #admin = await get_toxic_ticket_admin(task.issuer)
    # Allow anyone to issue TT's for testing
    admin = True
    user = await get_user_by_name_service(task.username) 
    if not user:
        user = User(
            username=task.username,
            email='notimplemented@test.com',
            discord_id=task.username,
            mini_toxic_tickets=0,
            toxic_tickets=0,
            pma_stickers=0
        )
        await add_user_service(user)
    user = await get_user_by_name_service(task.username)
    match task.ticket_type:
        case 'toxic_ticket':
            updated_user = await add_toxic_ticket_service(user.id, task.amount, admin)
        case 'mini_tt':
            updated_user = await add_mini_toxic_ticket_service(user.id, task.amount, admin)
        case 'pma_sticker':
            updated_user = await add_pma_sticker_service(user.id, task.amount, admin)
        case _:
            return errors.UnexpectedError("Unknown ticket type recieved")
    await send_message_to_server({ 
        'updated_user': updated_user, 
        'action': task.ticket_type, 
        'amount': task.amount, 
        'issuer': task.issuer,
        'channel': task.channel
    })
