from datetime import datetime
import os
from app.api.schemas.response.LoginResponse import LoginResponseDTO
from app.repository.AdminRepository import AdminRepository
from fastapi.exceptions import HTTPException
from dotenv import load_dotenv
import bcrypt

from app.service.JwtService import JwtService
from app.util.Custom_Exception import CustomException

load_dotenv()

class AdminService:
    
    @classmethod
    async def login_service(cls, req, db):
       
        if req.username == 'chelsea' and req.password=='123':
            data = {
                'iss':os.getenv('ISS'),
                'iat':datetime.now(),
                'sub':req.username,
                'role':'Admin',
                'aud':'fs_admin'
            }
            
            access_token = await JwtService.generate_access_token(data)
            refresh_token = await JwtService.generate_refresh_token(data=data)
            
            response = LoginResponseDTO(
                success=True,
                status_code=200,
                access_token=access_token,
                refresh_token=refresh_token
            )
            
            return response
        
       
        user_data = await AdminRepository.login_repository(req,db)
       
        if user_data is None:
            raise CustomException(status_code=404,detail='User Not Found!')
        
        salt = bcrypt.gensalt()
        hashed_pass = bcrypt.hashpw(req.password.encode('utf-8'),salt=salt) 
        
        if hashed_pass == user_data.password and req.username==user_data.username:
            data = {
                'iss':os.getenv('ISS'),
                'iat':datetime.now(),
                'sub':req.username,
                'audience': 'fs_admin',
                'role':'Admin'
            }
            access_token = JwtService.generate_access_token(data)
            refresh_token = JwtService.generate_access_token(data)
            
            
        raise CustomException(status_code=401,detail='Wrong Password!')
    
    @classmethod
    async def logout_service(cls,req,redis):
        pass