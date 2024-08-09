from dataclasses import asdict
from datetime import datetime

import bcrypt
from app.repository.DriverAuthRepo import DriverAuthRepo
from app.api.dto.response.DriverAuthResponse import DriverLoginResponse, DriverSignupResponse
from app.service.JwtService import JwtService


class DriverAuthService:
    @classmethod
    async def driver_signup_service(cls,driver_info,db):

        client_info.password = bcrypt.hashpw(driver_info.password.encode('utf-8'),bcrypt.gensalt()).decode('utf-8')
        client_info = asdict(driver_info)
        ok = await DriverAuthRepo.driver_signup_repo(driver_info,db)

        response = DriverSignupResponse(
            status_code=200,
            success=True,
            message='Driver Signup Successfull'
        )

        if not ok:
            response.status_code = 500
            response.message = "Couldn't sign up"

        return response

#     @classmethod
#     async def driver_login_service(cls,client_info,db):
#         user_info = await DriverAuthRepo.driver_login_repo(client_info,db)
       
#         password_match = bcrypt.checkpw(client_info.password.encode('utf-8'),user_info.get('password').encode('utf-8'))
#         data = {
#             "iss": "9493393e990ff8a4b5f88c68f2e23d16",
#             'iat':datetime.now(),
#             "sub": client_info.username,
#             "aud": "6a28d238a23fff3e43fc10c58dad9028",
#             "role": 'driver'
#         }
#         if user_info is not  None and password_match:
#             access_token = await JwtService.generate_access_token(data=data)    
#             refresh_token = await JwtService.generate_refresh_token(data=data)    
#             return DriverLoginResponse(
#                 status_code=200,
#                 success=True,
#                 message='Logged In successfully',
#                 acess_token=access_token,
#                 refresh_token=refresh_token
#             )
#         else:
#             return DriverSignupResponse(
#                status_code=404,
#                success=False,
#                message="Couldn't log in"
#            )
    
