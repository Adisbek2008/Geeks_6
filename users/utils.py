import redis
import random
import string
from django.conf import settings

REDIS_URL = getattr(settings, 'REDIS_URL', getattr(settings, 'REDIS_URL', 'redis://localhost:6379/0'))
redis_client = redis.from_url(REDIS_URL, decode_responses=True)

CONFIRMATION_TTL_SECONDS = 5 * 60

def _generate_code(length=6):
    return ''.join(random.choices(string.digits, k=length))

def save_confirmation_code(email_or_phone, code=None):
    if code is None:
        code = _generate_code()
    key = f"confirmation:{email_or_phone}"
    redis_client.setex(key, CONFIRMATION_TTL_SECONDS, code)
    return code

def verify_confirmation_code(email_or_phone, code):
    key = f"confirmation:{email_or_phone}"
    stored = redis_client.get(key)
    if stored is None:
        return False, "Код не найден или истёк."
    if stored != code:
        return False, "Неверный код."
    redis_client.delete(key)
    return True, "Код подтверждён."
