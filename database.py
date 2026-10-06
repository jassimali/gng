import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text


#"postgresql://username:password@localhost:5432/my_database"
load_dotenv()
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")


engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) 



with SessionLocal() as session:
    # Use text() to safely format your raw SQL query
    query = text("SELECT uid, username FROM users")
    
    # Execute and pass parameters as a dictionary
    result = session.execute(query)
    
    # Fetch data (returns Row objects)
    for row in result:
        print(f"ID: {row.uid}, Name: {row.name}")