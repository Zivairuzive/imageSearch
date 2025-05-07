from  app.db.db import Database

async def init_db():
    await Database.init_models()