from fastapi import APIRouter
from pydantic import BaseModel

router=APIRouter(
    prefix="/user",
    tags=['routers']
)

@router.post("/t1",tags=['intro'])
def test1():
    return "User added successfully"



