from redis_om import get_redis_connection

redis = get_redis_connection(
    host="redis-12158.crce179.ap-south-1-1.ec2.cloud.redislabs.com",
    port=12158,
    password="bioBrMgKAeZcKhi6BDy01uWtX3iklwsF",
    decode_responses=True
)