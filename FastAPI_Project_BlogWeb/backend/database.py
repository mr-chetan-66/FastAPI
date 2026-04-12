## Database Definition-------------------------------------
# Database creation boilerplate code:

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
 
SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://postgres:12345@localhost:5432/fastapi_db"
 
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# SQLALCHEMY_DATABASE_URL = "sqlite:///./fastapi-post.db"
 
# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
# )

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
 
Base = declarative_base() #A special class that remembers all models that inherit from it.

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
 