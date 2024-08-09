from dataclasses import asdict
from datetime import datetime

import bcrypt
from app.api.dto.response.ClientAuthResponse import ClientLoginResponse, ClientSignupResponse
from app.repository.ClientAuthRepo import ClientAuthRepo
from app.service.JwtService import JwtService


class ClientAuthService:
    @classmethod
    async def client_signup_service(cls,client_info,db):

        client_info.password = bcrypt.hashpw(client_info.password.encode('utf-8'),bcrypt.gensalt()).decode('utf-8')
        client_info = asdict(client_info)
        ok = await ClientAuthRepo.client_signup_repo(client_info,db)

        response = ClientSignupResponse(
            status_code=200,
            success=True,
            message='User Signup Successfull'
        )

        if not ok:
            response.status_code = 500
            response.message = "Couldn't sign up"

        return response

    @classmethod
    async def client_login_service(cls,client_info,db):
        user_info = await ClientAuthRepo.client_login_repo(client_info,db)
       
        password_match = bcrypt.checkpw(client_info.password.encode('utf-8'),user_info.get('password').encode('utf-8'))
        data = {
            "iss": "9493393e990ff8a4b5f88c68f2e23d16",
            'iat':datetime.now(),
            "sub": client_info.username,
            "aud": "6a28d238a23fff3e43fc10c58dad9028",
            "role": 'user'
        }
        if user_info is not  None and password_match:
            access_token = await JwtService.generate_access_token(data=data)    
            refresh_token = await JwtService.generate_refresh_token(data=data)    
            return ClientLoginResponse(
                status_code=200,
                success=True,
                message='Logged In successfully',
                acess_token=access_token,
                refresh_token=refresh_token
            )
        else:
            return ClientSignupResponse(
               status_code=404,
               success=False,
               message="Couldn't log in"
           )
    
    @classmethod
    async def client_order_service(cls,order_info, db):
        order_info = asdict(order_info)
        ok = await ClientAuthRepo.client_order_repo(order_info,db)
        return ok