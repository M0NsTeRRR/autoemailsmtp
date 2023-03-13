import logging
from typing import Optional

from pydantic import BaseSettings, HttpUrl, validator


class Settings(BaseSettings):
    LOG_LEVEL: logging.Logger
    SMTP_HOST: str
    SMTP_PORT: int = 587
    SMTP_USERNAME: str
    SMTP_PASSWORD: str
    DISCORD_WEBHOOK_URL: Optional[HttpUrl]

    @validator("LOG_LEVEL", pre=True)
    def assemble_cors_origins(cls, v: str):
        return logging.getLogger(v)

    @validator("SMTP_PORT", pre=True)
    def check_port_is_valid(cls, v: str) -> int:
        v = int(v)
        if not 1 <= v <= 65535:
            return ValueError(v)
        return v

    class Config:
        env_prefix = "AUTOEMAILSMTP_"
        env_file = ".env"


def get_settings() -> Settings:
    return Settings()
