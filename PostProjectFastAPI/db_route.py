
import shutil

from fastapi import APIRouter,Depends,UploadFile,File
from sqlalchemy.orm.session import Session
import db_func
from schema import PostBase, PostDisplay
from typing import List
import random,string

from database import get_db

router=APIRouter(prefix='/post',tags=['post'])

@router.post('/add',response_model=PostDisplay)
def create_post(request:PostBase,db:Session=Depends(get_db)):
    return db_func.create_post(db,request)

@router.get("/get",response_model=List[PostDisplay])
def get_all_post(db:Session=Depends(get_db)):
    return db_func.get_all_post(db)

@router.delete('delete/{id}',response_model=PostDisplay)
def delete_post(id:int,db:Session=Depends(get_db)):
    return db_func.delete_post(id,db)

@router.post('/upload_file')
def upload_file(image:UploadFile=File(...)):
    letters=string.ascii_letters
    rand_str=''.join(random.choice(letters) for _ in range(6))
    new=f'_{rand_str}.'
    filename=new.join(image.filename.rsplit('.',1))
    path=f'images/{filename}'
    
    with open(path,"wb+") as f:
        shutil.copyfileobj(image.file,f)
        
    return {
        'filename':path
    }
        
    