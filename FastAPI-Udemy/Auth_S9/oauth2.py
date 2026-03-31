from fastapi import Depends,HTTPException,status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from typing import Optional
from datetime import datetime, timedelta
from jose import jwt,JWTError
from db2 import db_func2
from db2.database2 import get_db
 
 
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


# When you write:
# TypeScriptoauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")Show more lines
# You are telling FastAPI & Swagger:

# Where the user can obtain the token

# Swagger shows a login form using this tokenUrl
# That form calls your backend's /token endpoint
# User enters username/password → gets JWT

# THIS DOES NOT run during authentication

# FastAPI never calls this tokenUrl during protected requests
# It does not fetch or refresh tokens

# Real apps NEVER use this tokenUrl

# Only Swagger UI uses it
# React, Flutter, Android, etc. IGNORE it


# GET http://127.0.0.1:8000/read_article/5
# Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.fakePayload.sig

# So what does oauth2_scheme really do?
# When you call:
# Pythontoken: str = Depends(oauth2_scheme)``Show more lines
# FastAPI does this:

# Look at incoming HTTP request
# Check for header:
# Authorization: Bearer <your_jwt_here>


# Extract <your_jwt_here> and pass it to your function.

# That’s it.
# No API call.
# No redirect.
# No token fetching.
# tokenUrl="token" is only documentation for Swagger UI, not an actual call.