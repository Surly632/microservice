from dataclasses import dataclass
from pydantic import BaseModel, EmailStr, validator

@dataclass
class AdminLoginRequest(BaseModel):
    username:str=''
    email:EmailStr=''
    password: str