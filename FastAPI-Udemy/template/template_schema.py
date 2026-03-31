from pydantic import BaseModel

class ProductBase(BaseModel):
    title:str
    desc:str
    price:float