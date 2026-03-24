from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def get_data(name,age):
    return {"message":"HIi, Chetan Here, playing iwth FastAPI"}

@app.post("/")
def get_data():
    return {"message":"HIi, Chetan Here, playing iwth FastAPI"}

@app.post("/users")
def create_user():
    return {"msg": "User created"}


# import uvicorn

# if __name__ == "__main__":

#     uvicorn.run("main:app", reload=True)

# http://127.0.0.1:8000/?name=Chetan&age=22


# or 
# uvicorn main:app --reload

# •	 http://127.0.0.1:8000  — Your API root
# •	 http://127.0.0.1:8000/docs  — Automatic Swagger UI documentation
# •	 http://127.0.0.1:8000/redoc  — Automatic ReDoc documentation
#   curl "http://127.0.0.1:8000/?name=Chetan&age=22"

# curl -X POST http://127.0.0.1:8000/users \
#      -H "Content-Type: application/json" \
#      -d '{"name":"Chetan","age":22}'

# curl -i http://127.0.0.1:8000/ == pretty output

# curl -X GET "http://127.0.0.1:8000/?name=Chetan&age=22" \
#   -H "accept: application/json"


# 5. Pydantic Model (🔥 Most important in real projects)
# from pydantic import BaseModel

# class User(BaseModel):
#     name: str
#     age: int

# @app.get("/user")
# def get_user():
#     return User(name="Chetan", age=22)
# 6. Custom Response (Advanced)
# from fastapi.responses import JSONResponse

# return JSONResponse(content={"msg": "custom"}, status_code=201)
# 7. HTML Response
# from fastapi.responses import HTMLResponse

# return HTMLResponse("<h1>Hello</h1>")
# 8. File Response
# from fastapi.responses import FileResponse

# return FileResponse("file.pdf")


# HTTP Methods (Very Important 🔥)
# Method	Use
# @app.get()	Fetch data
# @app.post()	Create data
# @app.put()	Update full data
# @app.patch()	Update partial
# @app.delete()	Delete data


# 🧩 3. What is {} in endpoint?

# 👉 {} is path parameter

# Example:
# @app.get("/users/{user_id}")
# def get_user(user_id: int):
#     return {"user_id": user_id}
# 🔁 Call this API:
# http://127.0.0.1:8000/users/10

# ➡️ Output:

# {
#   "user_id": 10
# }
# 🔥 Path vs Query (IMPORTANT)
# Path param:
# @app.get("/users/{id}")

# ➡️ /users/10

# Query param:
# @app.get("/users")
# def get_user(id: int):

# ➡️ /users?id=10


from fastapi import FastAPI
 
app = FastAPI()
 
# GET — read/retrieve data
@app.get("/items")
def get_items():
    return [{"id": 1, "name": "Apple"}, {"id": 2, "name": "Banana"}]
 
# POST — create new data
@app.post("/items")
def create_item():
    return {"message": "Item created"}
 
# PUT — update existing data
@app.put("/items/{item_id}")
def update_item(item_id: int):
    return {"message": f"Item {item_id} updated"}
 
# DELETE — remove data
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return {"message": f"Item {item_id} deleted"}

# Path Parameters
# Path parameters are variable parts of the URL. FastAPI automatically extracts them and converts to the correct type.

# The {item_id} in the path becomes a parameter in the function
@app.get("/items/{item_id}")
def get_item(item_id: int):  # FastAPI converts string URL to int automatically
    return {"item_id": item_id, "name": "Sample Item"}
 
# If you visit /items/42, item_id will be 42 (integer)
# If you visit /items/abc, FastAPI returns a 422 Unprocessable Entity error automatically


# Query Parameters
# Query parameters are the key=value pairs after the ? in a URL. For example: /items?skip=0&limit=10

@app.get("/items")
def get_items(skip: int = 0, limit: int = 10):  # Default values make them optional
    return {"skip": skip, "limit": limit}
 
# URL: /items              → skip=0, limit=10  (defaults)
# URL: /items?skip=5       → skip=5, limit=10
# URL: /items?skip=5&limit=20  → skip=5, limit=20
 
# Optional parameters using Optional from typing
from typing import Optional
 
@app.get("/search")
def search_items(q: Optional[str] = None):  # None means fully optional
    if q:
        return {"result": f"Searching for: {q}"}
    return {"result": "No search query provided"}


# 2. Use multiple routes

# If you want optional behavior:

@app.get("/items/")
def read_items():
    return {"item_id": "default"}

@app.get("/items/{item_id}")
def read_item(item_id: int): # item_id=None
    return {"item_id": item_id}

