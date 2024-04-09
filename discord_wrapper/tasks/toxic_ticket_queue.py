from fastapi import Depends
from typing import Annotated, Any
from config.config import get_redis_connection

# Consider switching Any to an actually defined data type (for sending toxic ticket data)
async def add_ticket_to_user(username: str, ticket_data: Any): 
    pass
