from mimetypes import init

from fastapi import Depends, HTTPException, FastAPI, APIRouter

app = FastAPI()

def common_parameters(q: str | None = None):
    return {"q": q}

@app.get('/dep_inj')
def di(comm:dict=Depends(common_parameters)):
    return comm

# http://127.0.0.1:8000/items/?q=test123--------------------------

class PaginationParams:
    def __init__(self, skip: int = 0, limit: int = 10):
        self.skip = skip
        self.limit = limit
        
@app.get("/products/")
def list_products(pagination: PaginationParams = Depends()):
    return {"skip": pagination.skip, "limit": pagination.limit}

# http://127.0.0.1:8000/products/?skip=5&limit=20
# http://127.0.0.1:8000/products/?skip=10
# http://127.0.0.1:8000/products/---------------------------------

class User:
    def __init__(self,name:str='Chetan' , age:int=22):
        self.name=name
        self.age=age
    
@app.post('create_user')        
def create_user(name:str,age:int,password:str,user:User=Depends(User)):
    return{
        "Name":user.name,
        "Age":user.age
    }












# Reusable Security Dependencies

def get_token_header(token: str | None = None):
    if token != "secret-token":
        raise HTTPException(status_code=400, detail="Invalid token")
    
@app.get("/secure-data/")
def secure_data(token: str = Depends(get_token_header)):
    return {"secret": "value"}

# http://127.0.0.1:8000/secure-data/?token=secret-token
# http://127.0.0.1:8000/secure-data/?token=abc----------------------------

# Global (Router-Level) Dependencies
router = APIRouter(
    prefix="/admin",
    dependencies=[Depends(get_token_header)]
)

@router.get("/stats")
def admin_stats():
    return {"stats": "admin only"}

# Every endpoint inside this router requires the get_token_header dependency.
# before running any route in this router.
# If the dependency fails, the endpoint won’t run.
# So ALL /admin/* routes require a valid token.
# http://127.0.0.1:8000/admin/stats?token=secret-token
# http://127.0.0.1:8000/admin/stats?token=abc---------------------------------

#@router.get("/stats", dependencies=[Depends(get_token_header)]) --> if you want for specific operation

from fastapi import Depends
from sqlalchemy.orm import Session

@app.get("/users/")
def read_users(db: Session = Depends(get_db)):
    return db.query(User).all()

# http://127.0.0.1:8000/users/
# http://localhost:8000/users/ -------------------------------------

import sqlite3
from fastapi import FastAPI, Depends
from DB_2.database2 import SessionLocal, get_db

app = FastAPI()

def create_connection():
    return sqlite3.connect("test.db")

def get_connection():
    conn = create_connection()
    try:
        yield conn
    finally:
        conn.close()

@app.get("/test")
def test(conn = Depends(get_connection)):
    cursor = conn.cursor()
    cursor.execute("SELECT sqlite_version();")
    return {"version": cursor.fetchone()}

# Request comes in
#       ↓
# get_connection() runs
#       ↓
# conn = create_connection()
#       ↓
# yield conn  →  API endpoint uses the connection
#       ↓
# endpoint finishes
#       ↓
# finally → conn.close()
#       ↓
# Done!


# APIRouter allows you to group multiple endpoints together.
# Useful for:

# Organizing code
# Grouping endpoints (admin, users, auth, etc.)
# Applying shared dependencies
# Adding route prefixes

