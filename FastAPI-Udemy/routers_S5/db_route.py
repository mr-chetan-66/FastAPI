from typing import List
from fastapi import APIRouter,Depends,HTTPException
from custom_log import database_log
from schema_db import UserBase, UserDisplay
from sqlalchemy.orm import Session
from DB_S7.database import get_db
from DB_S7 import db_func


router=APIRouter(
    prefix='/db_user',
    tags=['db_user'],
    dependencies=[Depends(database_log)]
)


## CREATE USER
@router.post("/create",response_model=UserDisplay)
def create_user(request:UserBase,db:Session=Depends(get_db)):
    return db_func.create_user(request,db)

## READ ALL USER
@router.get("/read_all",response_model=List[UserDisplay])
def read_all(db:Session=Depends(get_db)):
    return db_func.read_all(db)


## READ ONE USER
@router.get("/read/{id}",response_model=UserDisplay)
def read_one(id:int,db:Session=Depends(get_db)):
    user=db_func.read_one(id,db)
    if user is None:
        raise HTTPException(status_code=404,detail='User Not Found')
    return user

## UPDATE USER
@router.put("/update/{id}",response_model=UserDisplay)
def update(id:int,request:UserBase,db:Session=Depends(get_db)):
    user=db_func.update(id,request,db)
    if user is None:
        raise HTTPException(status_code=404,detail='User Not Found')
    return user

## DELETE USER
@router.delete("/delete/{id}",response_model=UserDisplay)
def delete(id:int,request:UserBase,db:Session=Depends(get_db)):
    user=db_func.delete(id,db)
    if user is None:
        raise HTTPException(status_code=404,detail='User Not Found')
    return user
