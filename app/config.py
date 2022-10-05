from pydantic import BaseSettings, Field

class Settings(BaseSettings):
    oracle: str = Field(..., env='ORACLE_DATABASE_URL')

settings = Settings()