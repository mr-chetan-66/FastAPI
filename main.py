from fastapi import FastAPI
from routers import router_get
from routers import router_post

app=FastAPI()
app.include_router(router_get.router)
app.include_router(router_post.router)

# Normal home endpoint api 
@app.get("/user")
def start():
    return "Hii, I'm Fast, FastAPI"

