from fastapi import APIRouter
from pydantic import BaseModel

router=APIRouter(
    prefix="/user",
    tags=['user']
)

@router.post("/t1")
def test1():
    return "User added successfully"

class UserModel(BaseModel):
    name:str
    age:int
    format:str

@router.post("/model")
def m1(user:UserModel):
    # we can access model param like user.name,user.age
    return {"DATA":user}

@router.post("/model-param/{id}")
def m1(user:UserModel,id:int,nickname="Chintu"):
    # we can access model param like user.name,user.age
    return {"DATA":f"{user} , {id}, {nickname}"}