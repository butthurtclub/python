from invoke import Collection
from daemons.tasks import (
    run_daemon,
    run_manager
)

ns = Collection()
ns.add_task(run_daemon)
ns.add_task(run_manager)
