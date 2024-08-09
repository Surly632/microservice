from datetime import datetime
from enum import Enum
from sqlalchemy import ARRAY, Integer,DECIMAL, String, ForeignKey, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped,mapped_column,relationship
from sqlalchemy.dialects.postgresql import TIMESTAMP,ENUM as PSENUM

Base = declarative_base()

class Driver(Base):
    __tablename__='drivers'
    id:Mapped[int] = mapped_column(Integer,autoincrement=True,primary_key=True,unique=True,nullable=False)
    username:Mapped[str] = mapped_column(String(30),nullable=False,unique=True)
    first_name: Mapped[str] = mapped_column(String,nullable=False)
    last_name: Mapped[str] = mapped_column(String,nullable=False)
    email: Mapped[str] = mapped_column(String,nullable=False,unique=True)
    password: Mapped[str] = mapped_column(String,nullable=False)
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True),default=func.now(),nullable=False)
    updated_at: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True),default=func.now(),nullable=False,onupdate=True)

    def __repr__(self):
        return (
            f"id: {self.id}\n"
            f"first_name: {self.first_name}\n"
            f"last_name: {self.last_name}\n"
            f"username: {self.username}\n"
            f"email: {self.email}\n"
            f"password: {self.password}\n"
            f"created_at: {self.created_at}\n"
            f"updated_at: {self.updated_at}\n\n"
        )

# from app.config.database import engine
# async def create_table():
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.drop_all)
#         await conn.run_sync(Base.metadata.create_all)
#         await engine.dispose()

# import asyncio
# asyncio.run(create_table())