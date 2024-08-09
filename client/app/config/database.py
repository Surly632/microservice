import os
from sqlalchemy.ext.asyncio import create_async_engine,AsyncSession,async_sessionmaker

engine = create_async_engine(
    url=os.getenv('DATABASE_URL'),
    # echo=True
)

sessionlocal=async_sessionmaker(
    bind=engine,
    autoflush= False,
    expire_on_commit= False,
    class_= AsyncSession
)