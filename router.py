from fastapi import APIRouter, Depends

router = APIRouter()

import pymysql
import os
import dotenv

from models import Books, Book
from session import get_session

dotenv.load_dotenv(".env")
conn_dict = {
    "host": os.environ.get("MYSQL_HOST"),
    "user": os.environ.get("MYSQL_USER"),
    "password": os.environ.get("MYSQL_PASSWORD"),
    "port": int(os.environ.get("MYSQL_PORT")),
    "database": os.environ.get("MYSQL_DATABASE"),
}

connection = pymysql.connect(
    **conn_dict
)


@router.get("/")
async def books(db=Depends(get_session)):
    return db.query(Books).all()


@router.get("/:id")
async def books(id: int, db=Depends(get_session)):
    return db.query(Books).get(id)


@router.post("/")
async def books(book: Book, db=Depends(get_session)):
    db.add(Books(name=book.name))
    db.commit()

    return db.query(Books).all()


@router.put("/:id")
async def books(id: int, book: Book, db=Depends(get_session)):
    old_book = db.query(Books).get(id)
    old_book.name = book.name
    db.commit()
    return db.query(Books).all()


@router.delete("/:id")
async def books(id: int, db=Depends(get_session)):
    db.query(Books).filter_by(id=id).delete()
    return db.query(Books).all()
