from fastapi import Depends,APIRouter,HTTPException
from db2 import db_func2
from db2.database2 import get_db
from schema2 import ArticleBase, ArticleDisplay, UserBase, UserDisplay
from sqlalchemy.orm import Session
from auth_S9.oauth2 import verify_user_using_jwt
from custom_log import database_log, log

router=APIRouter(
    prefix='/db_route2',
    tags=['db_route2'],
    dependencies=[Depends(database_log)])

@router.post("/create_user",response_model=UserDisplay)
def create_user(request:UserBase,db:Session=Depends(get_db)):
    log("Create User",f"User {request.username} is created")
    return db_func2.create_user(request,db)

@router.get('/read_user/{id}',response_model=UserDisplay)
def read_user(id:int,db:Session=Depends(get_db),current_user:UserBase=Depends(verify_user_using_jwt)):
    user=db_func2.read_user(id,db)
    if user is None:
        raise HTTPException(status_code=404,detail='User Not Found')
    return user

@router.post("/create_article",response_model=ArticleDisplay)
def create_article(request:ArticleBase,db:Session=Depends(get_db)):
    return db_func2.create_article(request,db)

@router.get("/read_article/{id}")
def read_article(id:int,db:Session=Depends(get_db),current_user:UserBase=Depends(verify_user_using_jwt)):
    article=db_func2.read_article(id,db)
    if article is None:
        raise HTTPException(status_code=404,detail='Article Not Found')
    return {'data':article,
            'Current User':current_user}
    
