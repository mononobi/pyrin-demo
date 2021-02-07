# -*- coding: utf-8 -*-
"""
cli module.

to enable locale management for application, execute:
`python cli.py babel enable`

to enable migrations for application, execute:
`python cli.py alembic enable`

to create a new package for application, execute:
`python cli.py template package`

usage example:

`python cli.py alembic upgrade --arg value`
`python cli.py babel extract --arg value`
`python cli.py template package`
`python cli.py celery worker --arg value`
`python cli.py security token --arg value`
"""

import fire

from pyrin.cli.services import get_cli_groups
from pyrin.packaging.services import is_package_loaded
from pyrin.task_queues.celery.services import get_current_app

from demo import DemoApplication


app_instance = DemoApplication(scripting_mode=True)

if is_package_loaded('pyrin.task_queues.celery') is True:
    celery_app = get_current_app()


if __name__ == '__main__':
    fire.Fire(get_cli_groups())
