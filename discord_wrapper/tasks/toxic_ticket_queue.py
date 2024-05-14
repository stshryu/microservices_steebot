from fastapi import Depends
from typing import Annotated, Dict, get_type_hints, Type
from config.config import get_redis_connection, Settings
import json
import errors
import success


class ToxicTicket:
    """
    Mirrors the class schema we define in the toxic_ticket microservce.
    """
    def __init__(self, username: str, ticket_type: str, amount: int, issuer: str, channel: str):
        self.username = username
        self.ticket_type = ticket_type
        self.amount = amount
        self.issuer = issuer
        self.channel = channel 

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)

async def add_ticket_to_user(ticket_data: dict):
    result = await validate_ticket_data(ticket_data)
    return await push_event_to_queue(result.unpack())

async def get_user_statistics(user_data: dict):
    return await push_event_to_queue(user_data)

async def push_event_to_queue(data):
    client = await get_redis_connection()
    await client.publish(Settings().TOXIC_TICKET_CHANNEL, data.toJson()) \
    if isinstance(data, ToxicTicket) else \
    await client.publish(Settings().TOXIC_TICKET_CHANNEL, json.dumps(data))
    return success.Success({}) 

async def validate_ticket_data(ticket_data: dict):
    """
    Takes in ticket data and returns a valid ToxicTicket class if valid.

    Parameter:
        valid_attributes: dict 

    Returns:
        Success(Object<ToxicTicket>)
    """
    hints = get_type_hints(ToxicTicket.__init__)
    valid_attributes = { key: value for key, value in ticket_data.items() }

    # Find missing attributes
    missing_attributes = set(hints.keys()) - set(valid_attributes.keys())
    # Find invalid attributes
    invalid_attributes = [
        param for param in valid_attributes.keys() \
        if not isinstance(valid_attributes.get(param, False), hints[param])
    ]

    # Construct error if present
    invalid_fields = { val: f"{val} field is missing" for val in missing_attributes }
    invalid_fields.update(
        { val: f"{val} field type is incorrect. Expected type {hints[val].__name__}" \
         for val in invalid_attributes}
    )

    return errors.InvalidDataInput(invalid_fields) if invalid_fields else success.Success(ToxicTicket(**valid_attributes))
