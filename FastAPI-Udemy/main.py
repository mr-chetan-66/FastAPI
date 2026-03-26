from fastapi import FastAPI
from routers_S5 import router_get
from routers_S5 import router_post
from routers_S5 import db_route 
from DB_S7 import db_model
from DB_S7.database import engine
from routers_S5 import live_viewer

app=FastAPI()
app.include_router(router_get.router)
app.include_router(router_post.router)
app.include_router(db_route.router)
app.include_router(live_viewer.router)

# Normal home endpoint api 
@app.get("/user",tags=['intro'])
def start():
    return "Hii, I'm Fast, FastAPI"

## DB_S7 -- CREATE DATABASE --------------
db_model.Base.metadata.create_all(engine)



