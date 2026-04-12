
# import httpx
import requests
from fastapi import HTTPException
from model import Order
from schema import OrderCreate
from fastapi.background import BackgroundTasks
import time
from database import redis


def get_order_all():
    try:
        return [Order.get(pk) for pk in Order.all_pks()]
    except:
        raise HTTPException(status_code=404, detail="No Order found")

def get_order(pk:str):
    try:
        return Order.get(pk)
    except:
        raise HTTPException(status_code=404, detail="Order not found")

def post_order(request:OrderCreate,bgtask:BackgroundTasks):
    req_of_product=requests.get("http://localhost:8000/products/%s"%request.product_id)
    # async with httpx.AsyncClient() as client:
    #     req_of_product=await client.get(f"http://localhost:8000/products/{request.product_id}")

    if req_of_product.status_code != 200:
        raise Exception(400,"Inventory service error")
    product=req_of_product.json()

    order=Order(
        product_id=request.product_id,
        price=product['price'],
        fee=0.2*product['price'],
        total=1.2*product['price'],
        quantity=request.quantity,
        status='pending'
    )

    order.save()
    bgtask.add_task(order_completed,order.pk)
    return order.model_dump()

def order_completed(order_id: str):
    time.sleep(5)
    order = Order.get(order_id)
    order.save()

    payload = {
        "order_id": order.pk,
        "product_id": order.product_id,
        "quantity": order.quantity
    }

    redis.xadd("order_completed", payload, "*", maxlen=1000)
    order.status = "completed"
    order.save()

def delete_order(pk:str):
    try:
        Order.delete(pk)
    except:
        raise HTTPException(status_code=404, detail="No Order found")

    return {"message": "Order deleted"}

def delete_all_order():
    try:
        for pk in Order.all_pks():
            Order.delete(pk)
    except:
        raise HTTPException(status_code=404, detail="No Order found")

    return {"message": "All order deleted"}







# ---------------------------------------------------------------
# |   NAME / TERM          |              MEANING               |
# ---------------------------------------------------------------
# | request: Request       | Incoming request object in FastAPI |
# |                        | - Comes from starlette.requests    |
# |                        | - Represents the client's request  |
# |                        | - You can read JSON, headers, etc  |
# ---------------------------------------------------------------
# | requests (library)     | Outgoing request library           |
# |                        | - Python's "requests" package      |
# |                        | - Used to call other services/API  |
# |                        | - Example: requests.get(url)       |
# ---------------------------------------------------------------
# | FastAPI Body (Pydantic)| Recommended way to receive data    |
# |                        | - Automatic parsing & validation   |
# |                        | - No need for request.json()       |
# |                        | - Cleaner and safer                |
# ---------------------------------------------------------------
# | async / await          | Non‑blocking I/O in FastAPI        |
# |                        | - Helps handle many requests       |
# |                        | - Should be used with httpx, not   |
# |                        |   blocking requests library        |
# ---------------------------------------------------------------

# we will get only id and quantity to order
    # ✅ When your function is async:
    # It does not block the event loop


# httpx is a Python HTTP client.
# Meaning:
# It lets your Python code send HTTP requests (GET, POST, etc.) to other APIs or microservices.
# await client.get()
# means:
# “Start the HTTP request, and while waiting for response, DO NOT block. Let FastAPI handle other requests meanwhile.”
# So your API can serve 1000 concurrent users without blocking.

# with use for this
# TCP connections
# Connection pool
# Network sockets
# Background async tasks