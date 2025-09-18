from datetime import date
from django.core.exceptions import ValidationError

def validate_age_for_product_creation(user):
    birthdate = getattr(user, 'birthdate', None)
    if not birthdate:
        raise ValidationError("Укажите дату рождения, чтобы создать продукт.")
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    if age < 18:
        raise ValidationError("Вам должно быть 18 лет, чтобы создать продукт.")
    return True
