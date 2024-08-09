from fastapi import APIRouter, Depends
from app.api.dto.request.ClientRequestDto import *
from app.config.JwtBearer import JwtBearer
from app.dependency.db_dependency import get_db
from app.service.ClientAuthService import ClientAuthService

router = APIRouter(prefix='/client')

@router.post('/signup')
async def client_login(client_info:ClientSignupDto, db = Depends(get_db)):
    if db is None:
        print('db is not found!')
    return await ClientAuthService.client_signup_service(client_info,db)


@router.post('/login')
async def client_login(client_info:ClientLoginDto, db = Depends(get_db)):
    return await ClientAuthService.client_login_service(client_info,db)

@router.post('/order',dependencies=[Depends(JwtBearer(required_roles=['Admin','user']))])
async def make_order(order_info:ClientOrderDto, db = Depends(get_db)):
    return await ClientAuthService.client_order_service(order_info,db)