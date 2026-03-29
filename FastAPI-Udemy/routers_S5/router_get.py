from fastapi import APIRouter
from enum import Enum
from typing import Optional


router=APIRouter(
    prefix='/user',
    tags=["router"]
)

@router.get("/hey",tags=['intro'])
def start(speed:Optional[int]=None):
    return f"Hii, I'm {speed}x Fast, {speed}xFastAPI"

class Match(str,Enum):
    Test=90
    ODI=50
    T20=20

@router.get("/match/{type}",tags=['URLparam'])
def match(type:Match):
    return {'message':f'Its a {type.name} match, that is {type.value}-overs'}
    
# URL param api , by deafaut 1 
@router.get("/{speed}",tags=['URLparam'])
def start(speed:int):
    return f"Hii, I'm {speed}x Fast, {speed}xFastAPI"

# order matter if we write code like this even if we hit right url it will show error as it expect int not hey so put the literal one first or we can say put the url param api endpoint definition in last 

# @app.get("/user/hey")
# def start(speed:int):
#     return f"Hii, I'm {speed}x Fast, {speed}xFastAPI"

@router.get("/qp",tags=['intro'])
def noparam():
    return {"Greet":"Hii old fossil"}

# @app.get("/qp")
# def qparam(id:int,name:str="Bittu",age:int=18):
#     return {"Greet":f"Hii {name}, are you really {age}-years old"}
# this will n0t work as we have create to endpoint on same route so first one will remain and second one get skip , it a rule , not to have api on same route , instead we can use combination of path and query parameter to solve it 

@router.get("/qp/{id}",tags=['Both-param'])
def qparam(id:int,name:str="Bittu",age:int=18):
    return {"Greet":f"Hii {name}, are you really {age}-years old"}

# @app.get("/qp/{id}")
# def revqparam(id:int,age:int=19,name:str="Chintu"):
#     return {"Greet":f"Hii {age}, are you really {name}-years old"}
# this will not work as we pass keywor var arg so order doesnt matter here / though we have different fucn name but it is on same route


@router.get("/test-param/{id}/onpage/{pid}",tags=['Both-param'])
def test(id:int,pid:int,valid:bool=True , username:str="Chal_Chal_Awe"):
    return {"Testify":f"Test on {id} with page no {pid} is {valid} by {username}"}





