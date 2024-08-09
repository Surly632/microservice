from fastapi import APIRouter, Depends
from app.api.dto.request.DriverRequestDto import *
from app.config.JwtBearer import JwtBearer
from app.dependency.db_dependency import get_db
from app.service.DriverAuthService import DriverAuthService

router = APIRouter(prefix='/driver')

@router.post('/signup')
async def client_login(client_info:ClientSignupDto, db = Depends(get_db)):
    if db is None:
        print('db is not found!')
    return await DriverAuthService.driver_signup_service(client_info,db)

@router.post('/login')
async def client_login(client_info:ClientLoginDto, db = Depends(get_db)):
    return await DriverAuthService.driver_login_service(client_info,db)


