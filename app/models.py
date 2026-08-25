from sqlalchemy import String,func,DateTime,ForeignKey
from sqlalchemy.orm import Mapped, mapped_column,relationship
from datetime import datetime

from .database import Base


class Post (Base):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id",ondelete="CASCADE"), nullable=False)
    user= relationship("User")
    title: Mapped[str] = mapped_column(String, nullable=False)
    content: Mapped[str] = mapped_column(String,nullable=False)
    published : Mapped[bool]=mapped_column(server_default='True')
    created_at: Mapped[datetime] = mapped_column (DateTime(timezone=True),server_default=func.now())


class User (Base):
    __tablename__= "users"

    id : Mapped[int] = mapped_column(primary_key=True, nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    password:  Mapped[str] = mapped_column(String, nullable=False)
    created_at: Mapped[datetime] = mapped_column (DateTime(timezone=True),server_default=func.now())


class Votes(Base):
    __tablename__="votes"

    user_id: Mapped[int]= mapped_column(ForeignKey("users.id", ondelete="CASCADE"),primary_key=True)
    post_id: Mapped[int]= mapped_column(ForeignKey("posts.id", ondelete="CASCADE"),primary_key=True)