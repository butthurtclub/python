import redis
import random

redis_client = redis.StrictRedis(
    host='localhost',
    port=6379,
    db=0,
    decode_responses=True
)

class Manager:
    def __init__(self):
        self.daemon = redis_client.keys('daemon:*')[0]
        self.action_key = f'{self.daemon}:action'

    def run(self):
        while(True):
            print('Enter command:')
            command = input().strip()

            redis_client.set(self.action_key, command)

