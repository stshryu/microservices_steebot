import success
import errors
from services.subscriber import ToxicTicket

async def send_message(receipient: str, message: str, ctx: dict) -> bool:
    """
    Sends a message to the discord server that originally sent the request
    
    Parameters:
        message: str    - The message to send to the server
        ctx: dict       - The context from which the origin request appears

    Returns:
        bool            - True if message was sent successfully, False otherwise
    """
    server_id = ctx.server_id
    issuer = ctx.author_id

    # TODO: Send the message to the discord server using the discord.py wrapper
