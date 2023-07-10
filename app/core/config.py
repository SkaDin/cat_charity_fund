from pydantic import BaseSettings


class Setting(BaseSettings):
    """Класс настроек Pydanctic."""
    app_title: str = 'Кошачьи делишки'
    description: str = 'Фонд помощи усатым'
    database_url: str = 'sqlite+aiosqlite:///./fastapi.db'
    secret: str = 'SECRET'

    class Config:
        env_file = '.env'


settings = Setting()
