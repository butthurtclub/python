from invoke import task
from .daemon import Daemon
from .manager import Manager
from .client import Client

@task
def run_daemon(ctx):
    try:
        daemon = Daemon()
        daemon.run()
    except KeyboardInterrupt:
        daemon.kill()
        exit()

@task
def run_manager(ctx):
    try:
        manager = Manager()
        manager.run()
    except KeyboardInterrupt:
        exit()

@task
def connect_client(ctx):
    try:
        client = Client()
        client.connect()
    except KeyboardInterrupt:
        client.disconnect()
        exit()