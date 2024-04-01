from celery import Celery

app_celery = Celery(
    "worker",
    broker="redis://redis:6379",
    include=["webapp.integrations.celery_app.tasks"],
    debug=True,
    backend="redis://redis:6379",
)
