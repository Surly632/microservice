import json
import aioredis
from sqlalchemy import Select
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.model.ClientModel import Client, Order
from app.util.CustomJsonEncoder import CustomJSONEncoder

class ClientAuthRepo:
    @classmethod 
    async def client_signup_repo(cls,client_info: dict,db:AsyncSession):
        to_add = Client(**client_info)
        try:
            await  db.flush()
            db.add(to_add)
            await db.commit()
            return True
        except Exception as e:

            await db.rollback()
            print(e)
            return False

    @classmethod 
    async def client_login_repo(cls,client_info: dict,db:AsyncSession):

        try:
            stmt = Select(Client).where(Client.username==client_info.username)
            res = await db.execute(stmt)
            user_info = res.first()[0].__dict__
            user_info.pop("_sa_instance_state")
            return user_info
        except Exception as e:
            print(e)
            return None

    @classmethod
    async def client_order_repo(cls,order_info:dict, db:AsyncSession):
        redis = aioredis.from_url('redis://localhost:6379/1')
        to_add = Order(**order_info)

        try:
            db.add(to_add)
            await db.commit()
            await db.flush()
            to_add_dict = to_add.__dict__
            to_add_dict.pop("_sa_instance_state", None)
            print(to_add_dict)
            await redis.sadd('open_order',json.dumps(to_add_dict,cls=CustomJSONEncoder))
            return True
        except Exception as e:
            print(e)
            return False
