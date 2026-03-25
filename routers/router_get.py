from fastapi import APIRouter,status,Response,HTTPException
from enum import Enum
from typing import Optional

router=APIRouter(
    prefix='/user',
    tags=["user"]
)

@router.get("/hey")
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

# order matter if we write code like thsi eve f we hit right url it will show error as it expect int not hey so put the literal one first or we can say put the utl param api endpoint definition in last 

# @app.get("/user/hey")
# def start(speed:int):
#     return f"Hii, I'm {speed}x Fast, {speed}xFastAPI"

@router.get("/qp")
def noparam():
    return {"Greet":"Hii old fossil"}

# @app.get("/qp")
# def qparam(id:int,name:str="Bittu",age:int=18):
#     return {"Greet":f"Hii {name}, are you really {age}-years old"}
# this will nt work as we have create to endpoint on sma route so firts one will remain and second oen get skip , it a rule , not to have to api on same route , instead we can use combination of path and query parameter to solve it 

@router.get("/qp/{id}",tags=['Both-param'])
def qparam(id:int,name:str="Bittu",age:int=18):
    return {"Greet":f"Hii {name}, are you really {age}-years old"}

# @app.get("/qp/{id}")
# def revqparam(id:int,age:int=19,name:str="Chintu"):
#     return {"Greet":f"Hii {age}, are you really {name}-years old"}
# this will not work as we pass keywor var arg so order doesnt matter here / though we have different fucn name but it is on same route


@router.get("/test-param/{id}/onpage/{pid}",tags=['Both-param'])
def test(id:int=1,pid:int=1,valid:bool=True , username:str="Chal_Chal_Awe"):
    return {"Testify":f"Test on {id} with page no {pid} is {valid} by {username}"}


#Status code

@router.get("/status/{age}",status_code=status.HTTP_404_NOT_FOUND,tags=['Status code'])
def nofound(age:int,resp:Response):
    if age<18:
        resp.status_code=status.HTTP_425_TOO_EARLY
        return {"error":"Underage Balak"}
    elif age >65:
        resp.status_code=status.HTTP_406_NOT_ACCEPTABLE
        return {"error":"Overage BadaBalak(GHEE KHATAM)"}
    else:
        resp.status_code=status.HTTP_200_OK
        return {"message":"Eligible Voter"}

#or

@router.get("/status2/{age}",tags=['Status code'])
def nofound2(age: int):
    if age < 18:
        raise HTTPException(status_code=425, detail="Underage Balak")
    elif age >65:
        raise HTTPException(status_code=406, detail="Overage BadaBalak(GHEE KHATAM)")
    else:
        return {"message":"Eligible Voter"}
    
# S & D
@router.get("/S-D/{id}",tags=['S & D'],summary="First Way",description="First way to add summary and desc for API")
def test(id:int=1,valid:bool=True , username:Optional[str]="Chal_Chal_Awe"):
    return {"Testify":f"Test on {id} for S and D is {valid} by {username}"}

@router.get("/S-D2/{id}",tags=['S & D'])
def test2(id:int=1,valid:bool=True , username:Optional[str]="Chal_Chal_Awe"):
    """
    - **summary**="Second Way"
    - **description**="Second way to add summary and desc for API"
    """
    return {"Testify":f"Test on {id} for S and D is {valid} by {username}"}

@router.get("/S-D3/{id}",tags=['S & D'],summary="First Way",description="First way to add summary and desc for API",response_description="Checked")
def test3(id:int=1,valid:bool=True , username:Optional[str]="Chal_Chal_Awe"):
    return {"Testify":f"Test on {id} for S and D is {valid} by {username}"}