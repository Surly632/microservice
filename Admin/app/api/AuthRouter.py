import aioredis
from fastapi import APIRouter, Depends, Request
from app.api.schemas.request.admin_schema import AdminLoginRequest
from app.config.JwtBearer import JwtBearer
from app.dependency.db_dependency import get_db
from sqlalchemy.ext.asyncio import AsyncSession
     
from app.dependency.redis_dependency import get_redis_blocked_token
from app.service.AdminService import AdminService
from log_config import log

router = APIRouter(prefix="/admin")

@router.post("/login")
async def admin_login(admin_info : AdminLoginRequest, db:AsyncSession = Depends(get_db)):
    return await AdminService.login_service(admin_info,db)

@router.delete('/logout',dependencies=[Depends(JwtBearer())])
async def admin_logout(req:Request, redis:aioredis.Redis=Depends(get_redis_blocked_token)):
    token = req.headers['Authorization'].split(' ')[-1]
    await redis.sadd('blocked_token',token)
    return {
        'success':True,
        'message': 'Logout Successful'
    }