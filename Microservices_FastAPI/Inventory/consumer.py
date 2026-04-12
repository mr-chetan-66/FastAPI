from database import redis
from model import Product

STREAM='order_completed'
GROUP='inventory-group'

try:
    redis.xgroup_create(STREAM,GROUP,id='0',mkstream=True)
    print(f"--> Created consumer group: {GROUP}")
except:
    print(f"--> {GROUP}: Group Already Exists")

print("--> Inventory consumer running... Waiting for messages...\n")

while True:
    try:
        message=redis.xreadgroup(GROUP,STREAM,{STREAM:">"},count=10,block=1000)

        for stream_name,event in message:
            for msg_id,data in event:
                print("\n--> Received message from \'order_completed\'")
                print(f"--> Message ID: {msg_id}")
                print(f"--> Data: {data}")

                try:
                    product=Product.get(data['product_id'])
                    print(f"--> Updating product {product.pk}, subtracting {data['quantity']} units")
                    product.quantity-=int(data['quantity'])
                    product.save()
                    print("--> Inventory updated successfully")
                    redis.xack(STREAM, GROUP, msg_id)
                    print(f"--> Acknowledged message {msg_id}")
                except Exception as e:
                    print(f"--> Error updating inventory: {e}")
                    print("--> Sending refund event to refund_completed stream")

                    redis.xadd("refund_completed", data)
                    print("--> Refund event sent")

    except Exception as e:
        print(f"--> Error in consumer loop: {e}")
