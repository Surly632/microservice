from app.api.model.AdminModel import Base
from app.config.database import engine

async def create_db():
    async with engine.begin() as conn:
        try:
            await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)
            
            print('database table created!')
            
            await engine.dispose()
        except:
            print('could not create table')

import asyncio
asyncio.run(create_db())