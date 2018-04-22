import redis
import random

redis_client = redis.StrictRedis(
    host='localhost',
    port=6379,
    db=0,
    decode_responses=True
)

class Manager:
    class Command:
        COMMAND = 0
        RECIPIENTS = 1
        MESSAGE = 2

    def __init__(self):
        self.daemon = redis_client.keys('daemon:*')[0]
        self.action_key = f'{self.daemon}:action'
        self.actions = ['clients', 'notify']

    def get_clients(self):
        return [
            client.split(':')[-1] for client in redis_client.keys('client:*')
        ]

    def clients(self, **kwargs):
        print('\n'.join(self.get_clients()))

    def notify(self, message, client_key=None, **kwargs):
        client_list = client_key if client_key else self.get_clients()
        redis_client.set(
            self.action_key, f'{",".join(client_list)}:{message}'
        )

    def run(self):
        while(True):
            print('Enter command:')
            command = input().strip()

            params = {'message': None, 'client_key': None}

            data = command.split(':')

            if len(data) == 3:
                if data[self.Command.RECIPIENTS] == 'all':
                    params['client_key'] = self.get_clients()
                else:
                    params['client_key'] = data[self.Command.RECIPIENTS].split(',')
                params['message'] = data[self.Command.MESSAGE]


            if data[self.Command.COMMAND] in self.actions:
                getattr(self, data[self.Command.COMMAND])(**params)
