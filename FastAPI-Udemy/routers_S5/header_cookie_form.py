
from typing import Optional,List

from fastapi import APIRouter,Response,Header,Cookie,Form

router=APIRouter(prefix='/header',tags=['Header'])
product=['Laptop','Phone','Bluetooth']

@router.get('request')
def request_header(response:Response,custome_header:Optional[str]=Header(None)):
    ## to get working run api -> inspect -> network -> open api call
    response.set_cookie(key='test_cookie',value='This is test Cookie')
    return product 

@router.get('multi-request')
def multi_request_header(response:Response,custome_header:Optional[List[str]]=Header(None),test_cookie:Optional[str]=Cookie(None)):
    ## to get working run api -> inspect -> network -> open api call ,
    response.headers['response_custom_header']=', '.join(custome_header)
    return {
        "Product":product,
        "Custom Header":custome_header,
        "Cookie":test_cookie
    }

# COOKIES:: store infromation on browser
# HTML form data <form> ....</form>
# application/x-www-form-urlncoded

# name:str=Form(...)
# we need to install python-multipart

@router.post('/create_product_using_form')
def create_product_using_form(data:str=Form(...)):
    product.append(data)
    return product


from fastapi import APIRouter, Request, Response, Header, Cookie
from typing import Optional, List

router = APIRouter()

product = "Mobile"

@router.get("/multi-request_higher")
def multi_request_header(
    request: Request,
    response: Response,
    custom_header: Optional[List[str]] = Header(None),
    test_cookie: Optional[str] = Cookie(None)
):
    # ---------------------------
    # 1. Read all Request Headers
    # ---------------------------
    all_headers = dict(request.headers)

    # ---------------------------
    # 2. Add your custom headers
    # ---------------------------
    if custom_header:
        response.headers["response_custom_header"] = ", ".join(custom_header)

    # Add another example header
    response.headers["X-Server"] = "FastAPI-Demo-Server"

    # ---------------------------
    # 3. Read all cookies
    # ---------------------------
    all_cookies = request.cookies

    # ---------------------------
    # 4. Set new cookies
    # ---------------------------
    response.set_cookie(key="new_cookie", value="cookie_value_123")
    response.set_cookie(key="user_id", value="101")

    return {
        "Product": product,
        "Incoming_Custom_Header": custom_header,
        "Incoming_Cookies": {
            "test_cookie": test_cookie,
            "all_cookies": all_cookies
        },
        "All_Headers": all_headers,
        "Response_Headers_Added": {
            "response_custom_header": response.headers.get("response_custom_header"),
            "X-Server": response.headers.get("X-Server")
        }
    }

