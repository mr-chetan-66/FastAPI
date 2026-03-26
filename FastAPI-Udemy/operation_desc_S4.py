from fastapi import FastAPI,HTTPException,status,Response
from typing import Optional

app=FastAPI()

#Status code-------------------------------------

@app.get("/status/{age}",tags=['OPS Desc'])
def nofound(age:int,resp:Response):
    if age<18:
        resp.status_code=status.HTTP_425_TOO_EARLY
        return {"error":"Underage Balak"}
    elif age >65:
        resp.status_code=status.HTTP_406_NOT_ACCEPTABLE
        return {"error":"Overage BadaBalak(GHEE KHATAM)"}
    else:
        resp.status_code=status.HTTP_200_OK
        return {"message":"Eligible Voter"}

#or

@app.get("/status2/{age}",tags=['OPS Desc'])
def nofound2(age: int):
    if age < 18:
        raise HTTPException(status_code=425, detail="Underage Balak")
    elif age >65:
        raise HTTPException(status_code=406, detail="Overage BadaBalak(GHEE KHATAM)")
    else:
        return {"message":"Eligible Voter"}
    
# S & D -------------------------------------------------------
@app.get("/S-D/{id}",tags=['OPS Desc'],summary="First Way",description="First way to add summary and desc for API")
def test(id:int=1,valid:bool=True , username:Optional[str]="Chal_Chal_Awe"):
    return {"Testify":f"Test on {id} for S and D is {valid} by {username}"}

@app.get("/S-D2/{id}",tags=['OPS Desc'])
def test2(id:int=1,valid:bool=True , username:Optional[str]="Chal_Chal_Awe"):
    """
    - **summary**="Second Way"
    - **description**="Second way to add summary and desc for API"
    """
    return {"Testify":f"Test on {id} for S and D is {valid} by {username}"}

@app.get("/S-D3/{id}",tags=['OPS Desc'],summary="First Way",description="First way to add summary and desc for API",response_description="Checked")
def test3(id:int=1,valid:bool=True , username:Optional[str]="Chal_Chal_Awe"):
    return {"Testify":f"Test on {id} for S and D is {valid} by {username}"}