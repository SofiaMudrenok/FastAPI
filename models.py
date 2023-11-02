from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey

from fastapi import Query
from typing import Annotated

from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Author(Base):
    __tablename__ = "author"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True
    )
    name: Mapped[str] = mapped_column(String(124))

    def __repr__(self):
        return self.__dict__


class Books(Base):
    __tablename__ = "books"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(124))

    def __repr__(self):
        return self.__dict__


from pydantic import BaseModel


class Book(BaseModel):
    name: str
