from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from http import HTTPStatus
from fastapi import FastAPI
import uvicorn

from app.api.DriverAuthRouter import router as driver_auth_router

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
    
    @app.get('/')
    async def homePage():
        data = {
            'success': True,
            'message': 'Welcome to HomePage'
        }
        return JSONResponse(content=data, status_code=HTTPStatus.OK)
    
    # app.include_router(router=driver_auth_router)
    return app

app = __init__app()

if __name__ == '__main__':
    uvicorn.run('main:app', host='localhost', port=port, reload=True)