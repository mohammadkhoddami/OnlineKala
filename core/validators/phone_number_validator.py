import re
from django.core.exceptions import ValidationError

def validate_phone_number(value):
    if not re.match(r'^09\d{9}$', value):
        raise ValidationError('Phone number is not correct')
    return value