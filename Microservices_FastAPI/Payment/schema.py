from pydantic import BaseModel

class OrderCreate(BaseModel):
    product_id:str
    quantity:int

class OrderDisplay(BaseModel):
    product_id:str
    total:float
    quantity:int
    status:str