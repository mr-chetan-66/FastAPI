from mako.template import Template
from fastapi import APIRouter,Request
from fastapi.responses import HTMLResponse
from template.template_schema import ProductBase

router=APIRouter(prefix='/template',tags=['template'])

@router.post("/{id}",response_class=HTMLResponse)
def get_product(id:int, product:ProductBase):
    template=Template(filename='template/product.html')
    html=template.render(
        id=id,
        title=product.title,
        desc=product.desc,
        price=product.price
    )
    return HTMLResponse(content=html)