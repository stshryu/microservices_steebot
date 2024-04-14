from typing import Optional
import json

class RedisMessage:
    """
    Represents the redis message pub/sub DTO
    """
    def __init__(self, message):
        self.msgtype = message['type']
        self.pattern = message['pattern']
        self.channel = message['channel']
        try:
            self.data = json.loads(message['data'])
        except:
            self.data = message['data']
