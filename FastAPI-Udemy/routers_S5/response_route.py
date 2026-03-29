

import asyncio

import fastapi
from fastapi.responses import (
    JSONResponse,
    PlainTextResponse,
    HTMLResponse,
    FileResponse,
    StreamingResponse,
    RedirectResponse,
)
from fastapi.templating import Jinja2Templates
from fastapi import Request,Depends,APIRouter,Response
import time
from custom_log import log

router = APIRouter(prefix='/response',tags=['response'],dependencies=[Depends(log)])

templates = Jinja2Templates(directory="./templates")
product=['Laptop','Phone','Bluetooth']


# 1. JSONResponse (default)
@router.get("/json", response_class=JSONResponse)
async def json_res():
    return {"message": "This is JSONResponse example"}


# 2. PlainTextResponse
@router.get("/text", response_class=PlainTextResponse)
async def text_res():
    return "Hello, this is plain text!"


# 3. HTMLResponse
@router.get("/html", response_class=HTMLResponse)
async def html_res():
    html = """
    <html>
        <body>
            <h1>Hello from HTMLResponse!</h1>
        </body>
    </html>
    """
    return html

@router.get('product/{id}',responses={
    200:{
       'content':{
           'text/html':{
               'example':'<div> Product </div>'
           }
       },
       'description': 'Return the HTML fro an object' 
    },
    404:{
        'content':{
           'text/Plain':{
               'example':' Product Not Found'
           }
       },
       'description': 'A clear text error message'
    }
})

def get_product(id:int):
    p=product[id]
    if id>len(product):
        #raise HTTPException(status_code=404,detail='Product Not Found')
        return PlainTextResponse(status_code=404,content='Product Not Found',media_type='text/plain')
        
    html=f"""
    <html>
    <head>
    <style>
    .product{{
        text-align:center;
        weidth:500px;
        height:30px;
        background-color:lightblue;
        border: 2px inset green
    }}
    </style>
    </head>
    <div class="product"> {p} </div>
    """
    
    return Response(content=html,media_type='text/html')

# 4. FileResponse - sending file download
@router.get("/file")
async def file_res():
    return FileResponse("./requirement.txt", media_type="text/plain", filename="download.txt")


# 5. StreamingResponse - stream numbers over time
def generate_stream():
    for i in range(5):
        yield f"Chunk {i}\n"
        time.sleep(1)


@router.get("/stream")
async def stream_res():
    return StreamingResponse(generate_stream(), media_type="text/plain")


# 6. RedirectResponse
@router.get("/redirect")
async def redirect_res():
    return RedirectResponse(url="http://127.0.0.1:8000/live/users")

# 9. Raw Response – fully manual control
@router.get("/raw")
async def raw_res():
    content = "Raw Response with custom header"
    return Response(content=content, media_type="text/plain", headers={"X-Custom": "Yes"})


async def wait_for_movement(n:int):
    await asyncio.sleep(n)
    return 'ok'

@router.get('/get_all')
async def get_all(n:int):
    data=" ".join(product)
    await wait_for_movement(n)
    return Response(content=data,media_type='text/plain')



# ---------------------------------------------------------------
# | Route        | Response Type         | FastAPI Class         |
# ---------------------------------------------------------------
# | /json        | JSONResponse          | JSONResponse          |
# | /text        | PlainTextResponse     | PlainTextResponse     |
# | /html        | HTMLResponse          | HTMLResponse          |
# | /file        | FileResponse          | FileResponse          |
# | /stream      | StreamingResponse     | StreamingResponse     |
# | /redirect    | RedirectResponse      | RedirectResponse      |
# | /template    | TemplateResponse      | TemplateResponse      |
# | /raw         | Manual Response       | Response (Base Class) |
# ---------------------------------------------------------------

#  async helps with concurrency, not dependency.
 
 
#  templates = Jinja2Templates(directory="templates")
#  This means:

# You are initializing Jinja2 template engine
# You tell FastAPI:
# “Inside the folder named templates, my HTML files are stored.”


# response_class tells FastAPI HOW to format the response.

# FileResponse itself IS the response class, so no need to specify again.
# Your actual file = sample.txt
# Browser download name = download.txt


# media_type = MIME type
# Examples:

# "text/plain" → simple text file
# "text/html" → HTML file
# "application/json" → JSON
# "image/png" → PNG image
# "application/pdf" → PDF document

# Jinja2 will open hello.html, and replace variables inside it.

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