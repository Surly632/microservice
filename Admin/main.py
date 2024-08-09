from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi import FastAPI, HTTPException, Request, Response
import uvicorn

from app.util.Custom_Exception import CustomException

__AUTHOR__ = '<Abm Himel>'

port = 8082

@asynccontextmanager
async def lifespan(app: FastAPI):
    from log_config import log
    log.info(f'server running on port: {port}')
    yield
    log.info('server is shutting down...')

def __init__app():
   
    app = FastAPI(
        lifespan=lifespan,
        title='Fast Api with postgresql',
        description='This is a demo',
        version='1.0.0'
    )
    
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["GET", "POST", "HEAD", "OPTIONS", "PUT", "DELETE"],
        allow_headers=["*"]
    )
    
    @app.exception_handler(CustomException)
    async def custom_exception(req: Request, exc: CustomException):
        res={
            'status_code':exc.status_code,
            'detail':exc.detail
        }
        return JSONResponse(
            status_code=exc.status_code,
            content=res
        )
    
    @app.get('/')
    async def homePage():
        data = {
            'success': True,
            'message': 'Welcome to HomePage'
        }
        raise CustomException(status_code=404,detail='no Details for error')
    
    from app.api.AuthRouter import router as admin_route
    app.include_router(router=admin_route)

    return app

app = __init__app()


if __name__ == '__main__':
    uvicorn.run('main:app', host='localhost', port=port, reload=True)