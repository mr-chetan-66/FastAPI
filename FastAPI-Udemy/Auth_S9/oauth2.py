from fastapi import Depends,HTTPException,status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from typing import Optional
from datetime import datetime, timedelta
from jose import jwt,JWTError

from DB_2 import db_func2
from DB_2.database2 import get_db
 
 
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
 
SECRET_KEY = '754efb55dfb7bc90df8865e7ca2eca2e957f5ae35d30074e32b351d9767e2da1'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30
 
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
  to_encode = data.copy()
  if expires_delta:
    expire = datetime.utcnow() + expires_delta
  else:
    expire = datetime.utcnow() + timedelta(minutes=15)
  to_encode.update({"exp": expire})
  encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
  return encoded_jwt


def verify_user_using_jwt(token:str=Depends(oauth2_scheme),db:Session=Depends(get_db)):
  credential_exception=HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail='Unauthorize Access',
    headers={'WWW-Authenticate': 'Bearer'}
  )
  try:
    payload=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
    
    username=payload.get("sub")
    if username is None:
      raise credential_exception
  except JWTError:
    raise credential_exception
  
  user=db_func2.read_user_by_username(username,db)
  if user is None:
    raise credential_exception 
  
  return user