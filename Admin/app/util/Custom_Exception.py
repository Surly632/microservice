class CustomException(Exception):
    def __init__(self,status_code,detail) -> None:
        self.status_code = status_code
        self.detail=detail
        super().__init__(status_code,detail)