import redis
from django.conf import settings

r = redis.Redis(
    host=getattr(settings, "REDIS_HOST", "localhost"),
    port=getattr(settings, "REDIS_PORT", 6379),
    db=0,
    decode_responses=True  
)

def save_code(user_id: int, code: str, ttl: int = 300):
    r.set(f"confirmation:{user_id}", code, ex=ttl)

def get_code(user_id: int) -> str | None:
    return r.get(f"confirmation:{user_id}")

def delete_code(user_id: int):
    r.delete(f"confirmation:{user_id}")
