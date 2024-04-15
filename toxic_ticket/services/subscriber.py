import success
import errors
import json
from config.config import get_redis_connection, Settings
from services.utils.redis_message import RedisMessage
from services.user import *

class ToxicTicket:
    """
    Mirrors the class schema we use in the discord_wrapper microservice.
    """
    def __init__(self, username: str, ticket_type: str, amount: int, issuer: str, ctx: dict):
        self.username = username
        self.ticket_type = ticket_type
        self.amount = amount
        self.issuer = issuer
        self.ctx = ctx

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)


async def process_channel():
    client = await get_redis_connection()
    channel = client.pubsub()
    await channel.subscribe(Settings().TOXIC_TICKET_CHANNEL)
    async for message in channel.listen():
        redis_msg = RedisMessage(message)
        if redis_msg.msgtype != 'subscribe': await process_message(redis_msg.data)

async def process_message(message):
    task = ToxicTicket(**message)
    admin = await get_toxic_ticket_admin(task.issuer)
    user = await get_user_by_name_service(task.username)
    if user:
        match task.ticket_type:
            case 'toxic_ticket':
                updated_user = await add_toxic_ticket_service(user.id, task.amount, admin)
            case 'mini_tt':
                updated_user = await add_mini_toxic_ticket_service(user.id, task.amount, admin)
            case 'pma_sticker':
                updated_user = await add_pma_sticker_service(user.id, task.amount, admin)
            case _:
                return errors.UnexpectedError("Unknown ticket type recieved")
    else:
        return errors.UnexpectedError("Unable to complete task")
