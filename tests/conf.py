from pathlib import Path

from starlette import status

BASE_DIR = Path(__file__).parent
FIXTURES_PATH = BASE_DIR / 'fixtures'


URLS = {
    'api': {
        'v1': {
            'task': '/api/v1/task',
            'task_stop': '/api/v1/task/stop',
        }
    }
}

DATA_LIST = [
    (0, status.HTTP_200_OK, [FIXTURES_PATH / 'robot.task.json']),
    (999, status.HTTP_404_NOT_FOUND, [FIXTURES_PATH / 'robot.task.json']),
]
