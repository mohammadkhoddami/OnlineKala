import random
from django.conf import settings
import redis


redis_client = redis.Redis(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT,
    db=settings.REDIS_DB,
    password=settings.REDIS_PASSWORD,
    decode_responses=True
)

def generate_otp_code():
    return str(random.randint(1000, 9999))


def set_value(key: str, value: str, ttl: int = 180):
    redis_client.setex(key, ttl, value)
    
def get_value(key: str):
    val = redis_client.get(key)
    return val if val else None

def delete_value(key: str):
    redis_client.delete(key)