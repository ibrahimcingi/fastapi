from pydantic_settings import BaseSettings
import os
from urllib.parse import urlparse

class Settings(BaseSettings):
  database_hostname:str
  database_port:str
  database_password:str
  database_name:str
  database_username:str
  secret_key:str
  algorithm:str
  access_token_expire_minutes:int

  class Config:
    env_file=".env"

settings=Settings()


if os.getenv("DATABASE_URL"):
    url = urlparse(os.getenv("DATABASE_URL").replace("postgres://", "postgresql://", 1))
    settings.database_hostname = url.hostname
    settings.database_port = str(url.port)
    settings.database_name = url.path[1:]
    settings.database_username = url.username
    settings.database_password = url.password