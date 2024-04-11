from fastapi import Depends
from typing import Annotated, Dict, get_type_hints
from config.config import get_redis_connection
import json
import errors
import success

# Consider switching Any to an actually defined data type (for sending toxic ticket data)
async def add_ticket_to_user(username: str, ticket_data: Dict[str, str]): 
    test = {"username": "gavin", "ticket_type": "test", "amount": "test amount", "issuer": "test"}
    res = await validate_ticket_data(test)
    return None

async def validate_ticket_data(ticket_data: Dict[str, str]):
    """
    Takes in ticket data and returns a valid ToxicTicket class if valid.

    Parameter:
        ticket_data: Any

    Returns:
        Object<ToxicTicket>
    """
    hints = get_type_hints(ToxicTicket.__init__)
    ## TODO Finish method
    valid_object = { key: value for key, value in ticket_data.items() if key in valid_attributes }
    return None

class ToxicTicket:
    __fieldvalidation__ = [
        "username",
        "ticket_type",
        "amount",
        "issuer"
    ]

    def __init__(self, username: str, ticket_type: str, amount: int, issuer: str):
        self.username = username
        self.ticket_type = ticket_type
        self.amount = amount
        self.issuer = issuer

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)
