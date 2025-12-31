import jwt
from datetime import datetime, timedelta
from django.conf import settings

def generate_jwt(user):
    payload = {
        'user_id': user.id,
        'email':user.email,
        'exp': datetime.utcnow() + timedelta(hours=1),
        'iat': datetime.utcnow(),
    }
    return jwt.encode(payload, settings.SECRET_KEY, algorithm='HS512')

def decode_jwt(token):
    return jwt.decode(token, settings.SECRET_KEY, algorithms=['HS512'])
