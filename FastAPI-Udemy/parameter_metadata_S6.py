from pydantic import BaseModel
from fastapi import FastAPI,Query,Body,Path
from typing import Optional,List,Dict

app=FastAPI()


##REQUEST BODY
class UserModel(BaseModel):
    name:str
    age:int
    format:str

@app.post("/model",tags=['parameter'])
def m1(user:UserModel):
    # we can access model param like user.name,user.age . This is request bidy exampel where we need to insert dta in json format when we hit the url 
    return {"DATA":user}

#this is example of request body with both param

@app.post("/model-param/{id}",tags=['parameter'])
def m1(user:UserModel,id:int,nickname="Chintu"):
    # we can access model param like user.name,user.age
    return {"DATA":f"{user} , {id}, {nickname}"}

##VALIDATOR
#parameter metadata # import Query  
@app.get("/metadata/{id}",tags=['parameter'])
def meta(user:UserModel,id:int,user_id:int=Query( 
    None,                                               ## added title and description
    title="user id",
    description=" User ID desc",
    alias="User ID",
    deprecated=True
    ),
        content:str=Body("Hi hwo are you "), # its a default value therefore optional by defalut that is if we dont provide it in json while hitting url it will still display default value
        #if we want to make is  non optional that is madatory then we have to use '...' or Ellipsis in place of default value
        number:int=Body(...,
                          min_length=10,
                          max_length=12,
                          regex='^[0-9]$'),
    ):
    return {
        "user":user,
        'id':id,
        'user_id':user_id,
        'Optional Content':content,
        'Require Content':number
    }


@app.get("/items",tags=['parameter'])
def read_items(search: str = Query(None, min_length=3), limit: int = 10):
    return {"search": search, "limit": limit}

    
# BODY--  describe how JSOn both should be 
# PATH--  describe how path param both should be 
# QUERY--  describe how query param both should be


## PARAMETER MULTIPLE VALUES
# Multiple value -- only query parameter can have multiple values
# URL EG-- ?User_ID=10&v=1.0&v=2.0&v=3.0 these value sent a slist to function

@app.get("/multi_value",tags=['parameter'])
def mv(v:Optional[List[str]]=Query(None)):
    return{
        'version':v #list of mutliple value display
    }
    
@app.get("/multi_value_default",tags=['parameter'])
def mvdefault(v:Optional[List[str]]=Query(['1.0','2.0','3.0'])):
    return{
        'version':v #list of mutliple value display
    }
    
## NUMBER VALIDATOR
@app.get("/nums1/{item_id}",tags=['parameter'])
def read_item(item_id: int = Path(..., gt=0,lt=10)):
    return {"item_id": item_id}

@app.get("/nums2/{item_id}",tags=['parameter'])
def read_item(item_id: int = Path(..., ge=0,le=10)):
    return {"item_id": item_id}

##COMPLEX SUBTYPE

class ImageModel(BaseModel):
    url:str
    desc:str

class BlogModel(BaseModel):
    name:str
    author:str
    tags:List[str]=[] #complex subtype with default empty list
    metadata:Dict[str,str]={'key1':'val1'} # we can pass any colection of python
    image:Optional[ImageModel]=None

    
