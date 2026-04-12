from fastapi import APIRouter
from schema import OrderCreate
from fastapi.background import BackgroundTasks
import db_func

router=APIRouter(
    prefix='/order',
    tags=['order']
)

@router.get("/all")
def get_order_all():
    return db_func.get_order_all()

@router.get("/{pk}")
def get_order(pk:str):
    return db_func.get_order(pk)

@router.post("/")
def post_order(request:OrderCreate,bgtask:BackgroundTasks):
    return db_func.post_order(request,bgtask)

@router.delete("/{pk}")
def delete_order(pk:str):
    return db_func.delete_order(pk)

@router.delete("/all")
def delete_all_order():
    return db_func.delete_all_order()
