from fastapi import Request,status#,HTTPException
from fastapi.responses import JSONResponse#,PlainTextResponse,

from fastapi import FastAPI ,Request,Body
from Auth_S9 import authetication_route
from DB_2.exception import StoryException
from routers_S5 import header_cookie_form, response_route
from routers_S5 import db_route2
from routers_S5 import router_get
from routers_S5 import router_post
from routers_S5 import db_route 
from DB_S7 import db_model
from DB_S7.database import engine
from routers_S5 import live_viewer
from DB_2 import db_model2
from DB_2.database2 import engine2
from fastapi.middleware.cors import CORSMiddleware


app=FastAPI()
app.include_router(db_route2.router)
app.include_router(authetication_route.router)
app.include_router(router_get.router)
app.include_router(router_post.router)
app.include_router(db_route.router)
app.include_router(live_viewer.router)
app.include_router(response_route.router)
app.include_router(header_cookie_form.router)

app.exception_handler(StoryException)
def story_exception_handler(request:Request,exec:StoryException):
    return JSONResponse(status_code=status.HTTP_418_IM_A_TEAPOT,content={'details':exec.message})


# app.exception_handler(HTTPException)
# def custom_handaler(request:Request,exec:StoryException):
#     return PlainTextResponse(str(exec),status_code=400)

# Normal home endpoint api 
@app.get("/user",tags=['intro'])
def start():
    return "Hii, I'm Fast, FastAPI"

## DB_S7 -- CREATE DATABASE --------------
db_model.Base.metadata.create_all(engine)
db_model2.Base.metadata.create_all(engine2)



## CORS -- Cross Origin Resource Sharing
# localhost:8080 <--> localhost:8000

origin=[
    'localhost:8080',
    'localhost:3000'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origin,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=['*']
)

# with this cors access allowed suppose my app running on localhost port 3000 and want to access any endpointy of fastapi by default it will not allowed so to allow access to certain origin we need to set allo origin 