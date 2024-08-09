from sqlalchemy import select

from app.api.model.AdminModel import Admin
from sqlalchemy.ext.asyncio import AsyncSession

class AdminRepository:
    
    @classmethod
    async def login_repository(cls,data, db:AsyncSession):
        stmt = select(Admin).where(Admin.username==data.username)
        res = await db.execute(stmt)
        res=res.first()
        return res