
from fastapi import status
from fastapi.responses import HTMLResponse,JSONResponse
from client import html
from fastapi import FastAPI ,Request,Body
from fastapi.websockets import WebSocket
from Auth_S9 import authetication_route
from DB_2.exception import StoryException
from routers_S5 import file, header_cookie_form, response_route
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
from fastapi.staticfiles import StaticFiles
import time


app=FastAPI()
app.include_router(file.router)
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


@app.get("/")
async def get():
    return HTMLResponse(html)

client=[]   #Every browser that connects via WebSocket gets stored here so we can send messages to everyone.

@app.websocket("/chat")
async def chat(websocket:WebSocket):
    await websocket.accept()
    client.append(websocket)
    while True:
        data= await websocket.receive_text()
        for c in client:
            await c.send_text(data)



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

@app.middleware("http")
async def add_middleware(request:Request,call_next):
    print("Before")
    start_time=time.time()
    response=await call_next(request)       #<-- actual api is hit 
    duration=time.time()-start_time
    response.headers["duration"]=str(duration)  
    print("After")
    return response

app.add_middleware(
    CORSMiddleware,
    allow_origins=origin,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=['*']
)

# with this cors access allowed suppose my app running on localhost port 3000 and want to access any endpointy of fastapi by default it will not allowed so to allow access to certain origin we need to set allo origin 
# In FastAPI, middleware is a function that runs before and/or after every request, allowing you to add common logic that applies to all routes.
# Think of middleware as a global filter that wraps your entire application.
# REQUEST → middleware → endpoint → middleware → RESPONSE

app.mount("/files",StaticFiles(directory='./Files_S10'),name='files')



## MIDDLEWARE ----------------------------------------
# response=await call_next(request)
#     Your middleware sits before the route.
# ✔️ call_next(request) means:

# “FastAPI, please run the actual endpoint (the route function) and give me its response.”
# USER
#   |
#   v
# Middleware (before)
#   |
#   |----> call_next(request) ----> Your endpoint ----> response
#   |
# Middleware (after)
#   |
#   v
# USER gets response


## WEBSOCKET BASED CHIT CHAT--------------------------------------
# User opens browser → http://localhost:8000
#             │
#             ▼
# FastAPI sends back HTML page
#             │
#             ▼
# HTML page runs JavaScript
#             │
#             ▼
# JavaScript opens WebSocket to ws://localhost:8000/chat  ← (THIS hits /chat)
#             │
#             ▼
# FastAPI websocket("/chat") runs
#             │
#             ▼
# await websocket.accept()   ← user connected
# client.append(websocket)   ← user added to chat list
#             │
#             ▼
# User sends a message → websocket.receive_text()
#             │
#             ▼
# Server sends message to all connected clients
#             │
#             ▼
# Browser displays message in chat box

# 🔹 FastAPI part = “backend”

# Accepts WebSocket connections
# Collects all connected users
# Sends each message to all users

# 🔹 HTML + JS part = “frontend”

# Displays messages
# Sends messages
# Keeps a real-time connection to backend


## TEMPLATES ----------------------------------
# Templates in FastAPI let you return HTML files instead of writing HTML inside Python code.
# Browser requests "/"
#         ↓
# FastAPI loads index.html from templates folder
#         ↓
# FastAPI fills {{ name }} with "Shrihari"
#         ↓
# Browser receives final HTML
#         ↓
# User sees "Hello Shrihari!"