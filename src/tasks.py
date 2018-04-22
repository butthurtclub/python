from invoke import Collection
from daemons.tasks import (
    run_daemon,
    run_manager,
    connect_client
)

ns = Collection()
ns.add_task(run_daemon)
ns.add_task(run_manager)
ns.add_task(connect_client)
