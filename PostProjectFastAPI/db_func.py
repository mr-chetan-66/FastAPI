

from sqlalchemy.orm.session import Session
from fastapi import HTTPException,status
from models import DbPost
from schema import PostBase
from datetime import datetime


def create_post(db:Session, request:PostBase):
    new_post=DbPost(
        image_url=request.image_url,
        title=request.title,
        content=request.content,
        creator=request.creator,
        timestamp=datetime.now()
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

def get_all_post(db:Session):
    users=db.query(DbPost).all()
    
    if not users :
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT,detail='Post Not Found')
    return users

def delete_post(id:int, db:Session):
    user=db.query(DbPost).filter(DbPost.id==id).first()
    if user is None:
        raise HTTPException(status_code=404,detail='Post Not Found')
    

    db.delete(user)
    db.commit()
    return user