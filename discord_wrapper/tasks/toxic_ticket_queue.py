from fastapi import Depends
from typing import Annotated, Dict 
from config.config import get_redis_connection
import json

# Consider switching Any to an actually defined data type (for sending toxic ticket data)
async def add_ticket_to_user(username: str, ticket_data: Dict[str, str]): 
    await validate_ticket_data({"hi", "hello"})
    return None

async def validate_ticket_data(ticket_data: Dict[str, str]):
    """
    Takes in ticket data and returns a valid ToxicTicket class if valid.

    Parameter:
        ticket_data: Any

    Returns:
        Object<ToxicTicket>
    """
    valid_attributes = ToxicTicket.__fieldvalidation__
    valid_object = { key: value for key, value in ticket_data if key in valid_attributes }
    return ToxicTicket(**valid_object)

class ToxicTicket:
    __fieldvalidation__ = [
        "username",
        "ticket_type",
        "amount",
        "issuer"
    ]

    def __init__(self, username: str, ticket_type: str, amount: int, issuer: str):
        self.username = username
        selt.ticket_type = ticket_type
        self.amount = amount
        self.issuer = issuer

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)
