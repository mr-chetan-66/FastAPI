from db2.db_model2 import DbArticle, DbUser
from db2.exception import StoryException
from db2.hash2 import Hash
from schema2 import ArticleBase, UserBase
from sqlalchemy.orm import Session

def create_user(request:UserBase,db:Session):
    new_user=DbUser(
        username=request.username,
        email=request.email,
        password=Hash.hash(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def read_user(id:int,db:Session):
    user=db.query(DbUser).filter(DbUser.id==id).first()
    if user is None:
        return None
    return user

def read_user_by_username(name:str,db:Session):
    user=db.query(DbUser).filter(DbUser.username==name).first()
    if user is None:
        return None
    return user

def create_article(request:ArticleBase,db:Session):
    if request.content.startswith('Once upon a time'):
        raise StoryException("No storytelling please.")
    new_article=DbArticle(
        title=request.title,
        content=request.content,
        published=request.published,
        user_id=request.customer_id
    )
    
    db.add(new_article)
    db.commit()
    db.refresh(new_article)
    return new_article

def read_article(id:int,db:Session):
    article=db.query(DbArticle).filter(DbArticle.id==id).first()
    if article is None:
        return None
    
    return article