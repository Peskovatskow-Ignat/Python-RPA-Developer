from webapp.integrations.postgres import engine
from webapp.models import meta


async def migrate() -> None:
    """Выполняет миграцию базы данных.

    Вызывает синхронную функцию `create_all` метаданных, чтобы создать все таблицы базы данных.

    """
    async with engine.begin() as conn:
        await conn.run_sync(meta.metadata.create_all)
