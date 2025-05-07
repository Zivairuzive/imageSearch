from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import sessionmaker
from app.core.config import settings
from app.db.base_model import BaseModel 

DATABASE_URL = "postgres+asyncpg://user:password@localhost/image_db"

class Database(object):
    def __init__(self, 
                url:str = settings.ASYNC_DATABASE_URL,
                echo:bool = settings.ECHO_SQL):
        self._engine = create_async_engine(url, echo=echo, pool_pre_ping = True)
        self.session_maker = async_sessionmaker(bind=self._engine, class_= AsyncSession, expire_on_commit=False)
        
    @property
    def engine(self):
        return self._engine
    
    def get_session(self)->AsyncSession:
        return self.session_maker()
    
    async def init_models(self):
        #loading models
        from app import models
        async with self.engine.begin() as conn:
            await conn.run_sync(BaseModel.metadata.create_all)
            


db = Database()
