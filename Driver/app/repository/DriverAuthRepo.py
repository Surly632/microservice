import json
import aioredis
from sqlalchemy import Select
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.model.DriverModel import Driver


class DriverAuthRepo:
    @classmethod
    async def driver_signup_repo(cls, driver_info: dict, db: AsyncSession):
        to_add = Driver(**driver_info)
        try:
            await db.flush()
            db.add(to_add)
            await db.commit()
            return True
        except Exception as e:

            await db.rollback()
            print(e)
            return False

    @classmethod
    async def driver_login_repo(cls, client_info: dict, db: AsyncSession):

        try:
            stmt = Select(Driver).where(Driver.username == client_info.username)
            res = await db.execute(stmt)
            user_info = res.first()[0].__dict__
            user_info.pop("_sa_instance_state")
            return user_info
        except Exception as e:
            print(e)
    #         return None

