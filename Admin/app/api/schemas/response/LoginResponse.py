
from dataclasses import dataclass

@dataclass
class LoginResponseDTO:
    success:str=None
    status_code:int=None
    access_token:str=None
    refresh_token:str=None