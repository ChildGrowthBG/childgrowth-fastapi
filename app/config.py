from dotenv import load_dotenv
from pydantic_settings import BaseSettings
from pydantic import computed_field


load_dotenv()


class Settings(BaseSettings):
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_NAME: str
    DB_PORT: int
    JWT_KEY: str

    @computed_field
    @property
    def DATABASE_URL(self) -> str:
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"


settings = Settings()
