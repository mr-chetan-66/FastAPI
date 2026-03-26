## ORM Functionality----------------------

from sqlalchemy.orm.session import Session
from schema_db import UserBase
from DB_S7.db_model import DbUser
from DB_S7.hash import Hash


def create_user(request:UserBase,db:Session):
    new_user=DbUser(
        username=request.username,
        email=request.email,
        password=Hash.hash(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def read_all(db:Session):
    return db.query(DbUser).all()

def read_one(id:int,db:Session):
    return db.query(DbUser).filter(DbUser.id==id).first()

def update(id:int,request:UserBase,db:Session):
    user=db.query(DbUser).filter(DbUser.id==id).first()
    if user is None:
        return None
    user.username=request.username
    user.email=request.email
    user.password=Hash.hash(request.password)
    db.commit()
    db.refresh(user)
    return user
    
    
def delete(id:int,db:Session):
    user=db.query(DbUser).filter(DbUser.id==id).first()
    if user is None:
        return None
    
    db.delete(user)
    db.commit()
    return user