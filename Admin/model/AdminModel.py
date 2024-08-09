from datetime import datetime
from sqlalchemy import Integer, String, func
from sqlalchemy.orm import declarative_base,Mapped,mapped_column
from sqlalchemy.dialects.postgresql import TIMESTAMP

Base = declarative_base()

class Admin(Base):
    __tablename__='admin'
    id: Mapped[int] = mapped_column(Integer,primary_key=True,nullable=False,autoincrement=True)
    username: Mapped[str] = mapped_column(String,nullable=False)
    password: Mapped[str] = mapped_column(String,nullable=False)
    created_by: Mapped[int] = mapped_column(Integer,nullable=False)
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True),default=func.now(),nullable=False)
    updated_at: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True),server_default=func.now(),onupdate=True,nullable=False)

    def __repr__(self):
        return (
            f"id: {self.id}\n"
            f"username: {self.username}\n"
            f"password: {self.password}\n"
            f"created_by: {self.created_by}\n"
            f"created_at: {self.created_at}\n"
            f"updated_at: {self.updated_at}\n\n"
        )
