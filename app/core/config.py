from pydantic import BaseSettings, PostgresDsn



class DataBaseSettings(BaseSettings):
    DATABASE_URL: PostgresDsn
    ASYNC_DATABASE: PostgresDsn
    ECHO_SQL = False
    
class Config:
    env_file = '.env'
    


settings = DataBaseSettings()