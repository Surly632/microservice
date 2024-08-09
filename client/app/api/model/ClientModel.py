from datetime import datetime
from enum import Enum
from sqlalchemy import ARRAY, Integer,DECIMAL, String, ForeignKey, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped,mapped_column,relationship
from sqlalchemy.dialects.postgresql import TIMESTAMP,ENUM as PSENUM

Base = declarative_base()

class Client(Base):
    __tablename__='clients'
    id:Mapped[int] = mapped_column(Integer,autoincrement=True,primary_key=True,unique=True,nullable=False)
    username:Mapped[str] = mapped_column(String(30),nullable=False,unique=True)
    first_name: Mapped[str] = mapped_column(String,nullable=False)
    last_name: Mapped[str] = mapped_column(String,nullable=False)
    email: Mapped[str] = mapped_column(String,nullable=False,unique=True)
    password: Mapped[str] = mapped_column(String,nullable=False)
    orders = relationship('Order',back_populates='clients',lazy='selectin')
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
class Status(Enum):
    active=1
    completed=2
    cancelled=3
    
class Order(Base):
    __tablename__= 'orders'
    id: Mapped[int] = mapped_column(Integer,primary_key=True,autoincrement=True,unique=True)
    item_name: Mapped[list[str]] = mapped_column(ARRAY(String),nullable=False)
    item_price: Mapped[list[float]] = mapped_column(ARRAY(DECIMAL),nullable=False)
    item_total: Mapped[float] = mapped_column(DECIMAL(10,3),nullable=False)
    status: Mapped[Status] = mapped_column(PSENUM(Status),nullable=False)
    client_id: Mapped[int] = mapped_column(Integer,ForeignKey('clients.id'),nullable=False)
    clients = relationship('Client',back_populates='orders',lazy='selectin')
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True),default=func.now(),nullable=False)
    updated_at: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True),default=func.now(),nullable=False,onupdate=True)


# from app.config.database import engine
# async def create_table():
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.drop_all)
#         await conn.run_sync(Base.metadata.create_all)
#         await engine.dispose()

# import asyncio
# asyncio.run(create_table())