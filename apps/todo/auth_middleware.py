from rest_framework.exceptions import AuthenticationFailed
from .jwt_utils import decode_jwt
from apps.accounts.models import User

def authenticate_request(request):
    token = request.META.get('HTTP_AUTHORIZATION', None)
    if not token:
        raise AuthenticationFailed("Token missing")

    token = token.replace("Bearer ", "")

    try:
        decoded = decode_jwt(token)
        return User.objects.get(id=decoded['user_id'])
    except:
        raise AuthenticationFailed("Invalid or expired token")
