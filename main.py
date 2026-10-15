from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
#from pwdlib import PasswordHash

from database import get_db,Base,engine
from models import User,Book
from schemas import UserCreate, UserResponse, BookCreate, BookResponse

app = FastAPI()


Base.metadata.create_all(bind=engine)

#password_hasher = PasswordHash.recommended()


@app.get("/")
def read_root():
    return {"message": "Hello, world!"}


@app.get("/hello/{name}")
def read_greeting(name: str):
    return {"message": f"Hello, {name}!"}


@app.get("/add")
def read_sum(a: int, b: int):
    return {"message": f"The sum of {a} and {b} is {a + b}"}


@app.get("/usersdata", response_model=list[UserResponse])
def read_userdata(db: Session = Depends(get_db)):
    users = db.scalars(select(User)).all()
    return users


@app.post("/newdata", response_model=UserResponse, status_code=201)
def write_data(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    new_user = User(
        id=user.id,
        name=user.name,
        age=user.age,
        email=str(user.email),
        password_hash=user.password
    )

    db.add(new_user)

    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=409,
            detail="A database constraint was violated"
        )

    db.refresh(new_user)

    return new_user

@app.post("/books", response_model=BookResponse, status_code=201)
def create_book(
    book: BookCreate,
    db: Session = Depends(get_db)
):
    new_book = Book(
        title=book.title,
        author=book.author,
        price=book.price,
        published_year=book.published_year
    )

    db.add(new_book)
    db.commit()
    db.refresh(new_book)

    return new_book

@app.get("/books", response_model=list[BookResponse])
def get_books(db: Session = Depends(get_db)):
    books = db.scalars(select(Book)).all()
    return books