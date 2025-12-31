from .models import User

class EmailOrUsernameBackend:
    """Authenticate using email or username and password against the minimal User model."""
    def authenticate(self, request, email=None, username=None, password=None, **kwargs):
        user = None
        if email:
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                return None
        elif username:
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                return None
        else:
            return None

        if user and user.check_password(password):
            return user
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
