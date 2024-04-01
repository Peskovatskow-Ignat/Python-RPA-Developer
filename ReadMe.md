Асинхронные процессы которые запускаются с помощью Fast Api
   - Модели: Task
  
Удалось реализовать:
- [x] Упаковка проекта в docker compose и запуск через docker compose up без дополнительной настройки
- [x] Прохождение flake8 + mypy в соответствии с конфигурациями проекта
- [x] Брокер сообщений через redis
- [x] Orm:  sqlalchemy2.0
- [x] Валидация входящих данных (pydantic)
- [x] Настройки в env
- [x] poetry как сборщик пакетов
- [x] Обработка ошибок и соответствующие статусы ответов

# Run
  
    git clone https://github.com/Peskovatskow-Ignat/Python-RPA-Developer.git
    
    cd Python-RPA-Developer

    docker compose up --build

# API

## methods
`/task` - creates new task 

>   curl -X 'POST' \
'http://127.0.0.1:8000/api/v1/task?start_number=0' \
  -H 'accept: application/json' \
  -d ''

`/task` - show all tasks

>   curl -X 'GET' \
  'http://127.0.0.1:8000/api/v1/task' \
  -H 'accept: application/json'

`/task/{task_id}` - returns task by id

>   curl -X 'GET' \
  'http://127.0.0.1:8000/api/v1/task/{task_id}' \
  -H 'accept: application/json'

`/task` - stopping the earliest task

>   curl -X 'PATCH' \
  'http://127.0.0.1:8000/api/v1/task' \
  -H 'accept: application/json'

`/task/{task_id}` - stopping task by id

>   curl -X 'PATCH' \
  'http://127.0.0.1:8000/api/v1/task/{task_id}' \
  -H 'accept: application/json'

# Docker compose
## App - web
> Container with FastAPI application 

## Celery

> Система для обработк сообщений

## Redis - redis

>Message Broker


# .env/.env.example
> BIND_PORT=8000
>
> BIND_IP=0.0.0.0
>    
>    
>    DB_URL=postgresql+asyncpg://postgres:postgres@web_db:5432/main_db
>    
>    REDIS_HOST=redis
>
>    REDIS_PORT=6379
>
>    REDIS_PASSWORD=
>    
