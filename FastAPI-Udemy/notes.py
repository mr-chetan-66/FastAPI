from logging import ERROR

from fastapi import FastAPI

app=FastAPI()

# @app.get("/")
# def get_data(name,age):
#     return {"message":"Hi, Chetan Here, playing iwth FastAPI"}

@app.post("/")
def get_data():
    return {"message":"HIi, Chetan Here, playing iwth FastAPI"}

# @app.post("/")
# def get_data():
#     return {"message":"HIi, Chetan Here, playing iwth FastAPI"}

# @app.post("/users")
# def create_user():
#     return {"msg": "User created"}


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


# from fastapi import FastAPI
 
# app = FastAPI()
 
# # GET — read/retrieve data
# @app.get("/items")
# def get_items():
#     return [{"id": 1, "name": "Apple"}, {"id": 2, "name": "Banana"}]
 
# # POST — create new data
# @app.post("/items")
# def create_item():
#     return {"message": "Item created"}
 
# # PUT — update existing data
# @app.put("/items/{item_id}")
# def update_item(item_id: int):
#     return {"message": f"Item {item_id} updated"}
 
# # DELETE — remove data
# @app.delete("/items/{item_id}")
# def delete_item(item_id: int):
#     return {"message": f"Item {item_id} deleted"}

# # Path Parameters
# # Path parameters are variable parts of the URL. FastAPI automatically extracts them and converts to the correct type.

# # The {item_id} in the path becomes a parameter in the function
# @app.get("/items/{item_id}")
# def get_item(item_id: int):  # FastAPI converts string URL to int automatically
#     return {"item_id": item_id, "name": "Sample Item"}
 
# # If you visit /items/42, item_id will be 42 (integer)
# # If you visit /items/abc, FastAPI returns a 422 Unprocessable Entity error automatically


# # Query Parameters
# # Query parameters are the key=value pairs after the ? in a URL. For example: /items?skip=0&limit=10

# @app.get("/items")
# def get_items(skip: int = 0, limit: int = 10):  # Default values make them optional
#     return {"skip": skip, "limit": limit}
 
# # URL: /items              → skip=0, limit=10  (defaults)
# # URL: /items?skip=5       → skip=5, limit=10
# # URL: /items?skip=5&limit=20  → skip=5, limit=20
 
# # Optional parameters using Optional from typing
# from typing import Optional
 
# @app.get("/search")
# def search_items(q: Optional[str] = None):  # None means fully optional
#     if q:
#         return {"result": f"Searching for: {q}"}
#     return {"result": "No search query provided"}


# # 2. Use multiple routes

# # If you want optional behavior:

# @app.get("/items/")
# def read_items():
#     return {"item_id": "default"}

# @app.get("/items/{item_id}")
# def read_item(item_id: int): # item_id=None
#     return {"item_id": item_id}

# Path and Query ---> always in URL
# body and pydantic model --> json payload/body


# STATUS CODE:

# 1XX ===    INFORMATIONAL
# 2XX ===    SUCCESS
# 3XX ===    REDIRECTION
# 4XX ===    CLIENT ERROR
# 5XX ===    SERVER ERROR

# Request is an object that contains everything the client sends to the server.
# When a browser or API client hits your FastAPI endpoint, the incoming HTTP request contains:

# URL (path)
# Query parameters
# Headers
# Cookies
# Form data
# JSON body
# Client IP
# Method (GET/POST/PUT etc.)
# Files uploaded

# FastAPI wraps all of this into a Request object.

## FASTAPI AUTHENTICATION --

# Headers are metadata sent with an HTTP request or response.
# They are NOT part of the body.
# ✔ Use cases
# Common examples:

# Authorization (Bearer tokens, API keys)
# Content-Type (JSON, HTML, file, etc.)
# User-Agent (browser/device info)
# CORS headers
# Custom metadata (X-Request-ID, X-Client-Version, etc.)

# from fastapi import FastAPI, Response, Cookie

# app = FastAPI()

# @app.get("/set-cookie")
# def set_cookie(response: Response):
#     response.set_cookie(key="session_id", value="abc123")
#     return {"message": "cookie set"}

# @app.get("/read-cookie")
# def read_cookie(session_id: str = Cookie(None)):
#     return {"session_id": session_id}

# OAuth2PasswordBearer tells FastAPI:

# "This API will receive a token from the user"
# "The token will be sent in the header: Authorization: Bearer <token>"</token>
# "tokenUrl='token'" means:
# The client must request the token from the /token endpoint.

# Your login/password are sent in the body of the request, NOT the URL.

# @router.post("/token")
# def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
#     user = authenticate(form_data.username, form_data.password)
#     token = create_access_token({"sub": user.username})
#     return {"access_token": token, "token_type": "bearer"}


# OAuth2PasswordRequestForm = Depends()
# This means:

# FastAPI automatically reads username/password from form data
# Not from the URL
# Not from query parameters
# Not from headers


# token: str = Depends(oauth2_scheme)
# FastAPI does:

# Look inside HTTP headers
# Find Authorization: Bearer <token>
# Extract the token
# Give the raw token string to your function

# That's it.
# No verification yet.


# FastAPI has a built-in OAuth2 system.
# When you write this:


# request: OAuth2PasswordRequestForm = Depends()

# FastAPI automatically extracts:

# username
# password

# from the request BODY


# 🔥 YOU HAVE TWO COMPLETELY SEPARATE PROCESSES
# 1️⃣ Token Generation (Login)
# Endpoint: /token

# User sends username/password
# Server checks DB
# Server creates JWT
# Returns JWT

# This is required by OAuth2 Password Flow.

# 2️⃣ Token Verification (Protected Endpoints)
# Your code validates token manually, e.g.:
# PythonDepends(get_current_user)Show more lines
# This step has nothing to do with /token.



# ✅ 1. Should you use async def in FastAPI?
# Yes — it is good practice to use async def for most FastAPI endpoints.
# Why?
# Because:
# ✔ Async functions allow concurrency
# FastAPI uses asyncio, which means while your API waits for I/O (database calls, file read, network requests), it can serve other users.
# ✔ Async avoids blocking the event loop
# If one request sleeps or waits for I/O, others can continue.
# ✔ Best for:

# Database queries
# Calling other APIs
# File reading/writing
# Background tasks
# Streaming
# Any I/O-bound work


# ❌ When you should NOT use async def?
# If your function performs CPU-heavy work:

# image processing
# machine learning computation
# heavy loops

# Then async does not help — and can even hurt performance.
# Use regular def in those cases.


# 2. When do you use await?
# Simple rule:
# 👉 You can only use await inside async def.
# 👉 You must use await when calling async functions.
# Example:
    
#     async def get_data():
#     return "hello"

# async def route():
#     x = await get_data()
#     return x