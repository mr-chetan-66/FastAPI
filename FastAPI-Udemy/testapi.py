from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

class User(BaseModel):
    name:str
    age:int

user_list:List[User]=[]

app=FastAPI()

@app.post("/")
def get_all_user(user:User):
    return user_list.append(user)

@app.get("/user/{name}")
def get_entity(name:str):
    for u in user_list:
        if(u.name==name):
            return u
    