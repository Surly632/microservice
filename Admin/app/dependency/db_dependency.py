from app.config.database import sessionlocal

async def get_db(): 
        try:
            async with sessionlocal() as db:
                await db.begin()
                yield db
        except Exception as e:
            raise e
        finally:
            await db.close()    

 