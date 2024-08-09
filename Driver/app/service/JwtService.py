from typing import Optional
from jose import jwt
from dotenv import load_dotenv
from datetime import datetime, timedelta
import os

load_dotenv()


class JwtService:

    __secret_key = os.getenv("SECRET_KEY")

    @classmethod
    async def generate_access_token(cls, data: dict, exp_time: Optional[timedelta] = None):
        to_encode = data.copy()
        if exp_time:
            expire = datetime.now() + exp_time
        else:
            expire = datetime.now() + timedelta(minutes=15)
        to_encode.update({"exp": expire.timestamp()})
        encoded_token = jwt.encode(to_encode, cls.__secret_key, algorithm="HS256")
        return encoded_token

    @classmethod
    async def generate_refresh_token(cls, data: dict, exp_time: Optional[timedelta] = None):
        to_encode = data.copy()
        if exp_time:
            expire = datetime.now() + exp_time
        else:
            expire = datetime.now() + timedelta(days=15)
        to_encode.update({"exp": expire.timestamp()})
        encoded_token = jwt.encode(to_encode, cls.__secret_key, algorithm="HS256")
        return encoded_token

    @classmethod
    async def decode_token(cls, token: str):
        try:
            data = jwt.decode(
                token,
                cls.__secret_key,
                algorithms=["HS256"],
                audience="6a28d238a23fff3e43fc10c58dad9028"
            )
            return data
        except jwt.ExpiredSignatureError:
            return None
        except jwt.JWTError:
            return None
        except Exception:
            return None