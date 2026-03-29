
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

