from sqlalchemy.ext.asyncio import AsyncSession,create_async_engine,async_sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

engine = create_async_engine(
    url=os.getenv('DATABASE_URL'),
    echo=True
)

sessionlocal = async_sessionmaker(
    bind=engine,
    autoflush=False,
    expire_on_commit=False,
    class_=AsyncSession
)



