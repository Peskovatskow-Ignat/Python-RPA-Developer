import asyncio

from webapp.integrations.celery_app.celery import app_celery


@app_celery.task()
def start_robot(data: dict[str, any]) -> None:
    start = data.get('start')
    task_id = data.get('task_id')
    while True:
        print(f'task_id: {task_id} | iter_number: {start}')
        start += 1
        from time import sleep

        sleep(1)
