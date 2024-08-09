
from dataclasses import dataclass
import re
from pydantic import BaseModel, EmailStr, validator

@dataclass
class ClientSignupDto(BaseModel):
    username: str
    first_name: str
    last_name : str
    email : EmailStr
    password: str
    
    # @validator("password",pre=True,always=True)
    # def validate_password(password: str):
    #     if not re.match('.*[-_@#{}^%$!].*',password):
    #         return False
    #     return password

@dataclass
class ClientLoginDto(BaseModel):
    username:str=None
    password:str=None
    
@dataclass 
class ClientOrderDto(BaseModel):
    item_name: list[str]
    item_price: list[float]
    item_total: float
    status:str
    client_id: int
          