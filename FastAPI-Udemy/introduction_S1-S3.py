from fastapi import FastAPI
from routers_S5 import router_get
from routers_S5 import router_post

app=FastAPI()
app.include_router(router_get.router)
app.include_router(router_post.router)

# Normal home endpoint api 
@app.get("/user",tags=['intro'])
def start():
    return "Hii, I'm Fast, FastAPI"

