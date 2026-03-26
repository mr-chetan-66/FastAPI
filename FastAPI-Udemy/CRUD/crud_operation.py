from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()

# ------------------------------
# Uber User Model
# ------------------------------
class UberUser(BaseModel):
    id: int
    name: str
    email: str
    phone: str
    default_location: Optional[str] = None
    preferred_payment: Optional[str] = None


# A REAL collection (List)
users: List[UberUser] = []


# ------------------------------
# POST - Create new user
# ------------------------------
@app.post("/users", status_code=201)
def create_user(user: UberUser):
    users.append(user)
    return {"message": "User created", "user": user}


# ------------------------------
# GET - Get all users
# ------------------------------
@app.get("/users")
def get_all_users():
    return users


# ------------------------------
# GET - Get single user
# ------------------------------
@app.get("/users/{user_id}")
def get_user(user_id: int):
    for user in users:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")


# ------------------------------
# PUT - Replace Entire User
# ------------------------------
@app.put("/users/{user_id}")
def replace_user(user_id: int, new_user: UberUser):
    for index, user in enumerate(users):
        if user.id == user_id:
            users[index] = new_user
            return {"message": "User replaced", "user": new_user}
    raise HTTPException(status_code=404, detail="User not found")


# ------------------------------
# PATCH - Update Partial Fields
# ------------------------------
@app.patch("/users/{user_id}")
def patch_user(user_id: int, updates: dict):
    for index, user in enumerate(users):
        if user.id == user_id:
            updated_data = user.dict()
            updated_data.update(updates)
            updated_user = UberUser(**updated_data)
            users[index] = updated_user
            return {"message": "User updated", "user": updated_user}

    raise HTTPException(status_code=404, detail="User not found")


# ------------------------------
# DELETE - Remove user
# ------------------------------
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    for index, user in enumerate(users):
        if user.id == user_id:
            users.pop(index)
            return {"message": "User deleted"}
    raise HTTPException(status_code=404, detail="User not found")