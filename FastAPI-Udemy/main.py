from fastapi import FastAPI
from routers_S5 import db_route2, router_get
from routers_S5 import router_post
from routers_S5 import db_route 
from DB_S7 import db_model
from DB_S7.database import engine
from routers_S5 import live_viewer
from DB_2 import db_model2
from DB_2.database2 import engine2

app=FastAPI()
app.include_router(router_get.router)
app.include_router(router_post.router)
app.include_router(db_route.router)
app.include_router(live_viewer.router)
app.include_router(db_route2.router)

# Normal home endpoint api 
@app.get("/user",tags=['intro'])
def start():
    return "Hii, I'm Fast, FastAPI"

## DB_S7 -- CREATE DATABASE --------------
db_model.Base.metadata.create_all(engine)
db_model2.Base.metadata.create_all(engine2)


