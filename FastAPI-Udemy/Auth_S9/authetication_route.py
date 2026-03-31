
from fastapi import APIRouter,Depends,HTTPException,status
from fastapi.security import OAuth2PasswordRequestForm
from auth_S9.oauth2 import create_access_token
from db2.database2 import get_db
from sqlalchemy.orm import Session

from db2.db_model2 import DbUser
from db2.hash2 import Hash

router=APIRouter(tags=['Auth'])

@router.post('/token')
def create_auth_token(data:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(get_db)):
    username=data.username
    password=data.password
    
    user=db.query(DbUser).filter(DbUser.username==username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Invalid Credential')
    
    if not Hash.verify(password,user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Incorrect Password')
    
    token=create_access_token(data={'sub':username})
    
    return {
        "access_token":token,
        "token_type":"bearer",
        "username":username,
        "user id": user.id
    }