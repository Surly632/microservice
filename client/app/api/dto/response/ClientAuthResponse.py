from dataclasses import dataclass


@dataclass
class ClientSignupResponse:
    status_code: int =None
    success: bool = None
    message: str =None

@dataclass
class ClientLoginResponse:
    status_code: int = None
    success: bool = None
    message: str = None
    acess_token:str=None
    refresh_token: str= None
