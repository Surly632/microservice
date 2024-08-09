from jose import jwt
from dotenv import load_dotenv
from datetime import datetime, timedelta
import os
load_dotenv()

class JwtService:   
     
    __secret_key = os.getenv('SECRET_KEY')

    @classmethod
    async def generate_access_token(self,data:dict , exp_time: timedelta=None):
        to_encode = data.copy()
        if exp_time:
            to_encode.update({'exp':exp_time})
        else:
            exp_time = datetime.now()+timedelta(minutes=15)
        
        encoded_token = jwt.encode(data,self.__secret_key,algorithm='HS256')
        
        return encoded_token
    
    @classmethod
    async def generate_refresh_token(self,data:dict , exp_time: timedelta=None):
        to_encode = data.copy()
        if exp_time:
            to_encode.update({'exp':exp_time})
        else:
            exp_time = datetime.now()+timedelta(days=15)
        
        encoded_token = jwt.encode(data,self.__secret_key,algorithm='HS256')
        
        return encoded_token
    
    @classmethod
    async def decode_token(self,token:str):
        try:
            data = jwt.decode(token,self.__secret_key,algorithm='HS256',audience='fs_admin')
            return data
        except:
            return None