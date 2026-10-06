import email

from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text

app = FastAPI()


#"postgresql://username:password@localhost:5432/my_database"
SQLALCHEMY_DATABASE_URL = "postgresql://localhost:5433/postgres"


engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) 


@app.get("/")
def read_root():
    return {"message": "Hello, world!"}


@app.get("/hello/{name}")
def read_greeting(name: str):
    return {"message": f"Hello, {name}!"}


@app.get("/add")
def read_sum(a: str, b: str):
    return {"message": f"The sum of {a} and {b} is {int(a) + int(b)}"}


@app.get("/userdata")
def read_userdata():
    with SessionLocal() as session:
        query = text("SELECT id, name, email FROM users")
        result = session.execute(query)
        data = [{"id": row.id, "name": row.name, "email":row.email} for row in result]
    return {"data": data}


@app.post("/newdata")
def write_data(id: int, name: str, age: int, email: str, password: str):
    with SessionLocal() as session:
        query = text(
            'INSERT INTO users (id, name, age, email, pass) '
            "VALUES (:id, :name, :age, :email, :password)"
        )
        session.execute(
            query,
            {
                "id": id,
                "name": name,
                "age": age,
                "email": email,
                "password": password,
            },
        )
        session.commit()
    return {"message": "Data added successfully"}