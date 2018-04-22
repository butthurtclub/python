from time import sleep
import redis
import random

redis_client = redis.StrictRedis(
    host='localhost',
    port=6379,
    db=0,
    decode_responses=True
)

class Client:
    def __init__(self):
        self.id = random.randint(1787, 9756)
        self.name = f'client:{self.id}'
        self.message_key = f'client:{self.id}:message'

    def connect(self):
        redis_client.set(self.name, 'registered')
        print(f'Client {self.id} connected')
        while(True):
            message = redis_client.get(self.message_key)
            if not message:
                sleep(1)
                continue
            print(message)
            redis_client.delete(self.message_key)

    def disconnect(self):
        redis_client.delete(self.name)
