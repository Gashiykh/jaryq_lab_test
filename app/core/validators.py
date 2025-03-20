from django.core.exceptions import ValidationError

def hour_range(value):
    if not (0 <= value <= 23):
        raise ValidationError("Таймслот должен быть от 0 до 23.")