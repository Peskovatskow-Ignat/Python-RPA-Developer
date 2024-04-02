from time import sleep

from webapp.integrations.celery_app.celery import app_celery


@app_celery.task()
def start_robot(data: dict[str, int]) -> None:
    """Задача запуска робота.

    Args:
        data (dict[str, int]): Словарь с данными, включающий:
            - 'start' (int): Начальное значение счетчика итераций. По умолчанию 0.
            - 'task_id' (int): Идентификатор задачи.
    """
    start: int = data.get('start', 0)
    task_id = data.get('task_id')
    while True:
        print(f'task_id: {task_id} | iter_number: {start}')
        start += 1
        sleep(1)
