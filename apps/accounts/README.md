This app uses a minimal custom `User` model with only the following fields:

- `id` (BigAutoField primary key)
- `username` (unique)
- `email` (unique)
- `password` (hashed string)

Auth flow summary:
- Registration: POST `/auth/register/` with `username`, `email`, `password`.
- Login: POST `/auth/login/` with `email`, `password` — returns a JWT token.
- Token decoding: `apps/todo/jwt_utils.py`
- Token-based auth helper: `apps/todo/auth_middleware.py` (returns the `User` instance).

Notes and next steps:
- Run `python -m pip install -r requirements.txt` and then `python manage.py makemigrations` and `python manage.py migrate` to apply changes.
- Since the app is intentionally minimal, `django.contrib.admin` has been removed from `INSTALLED_APPS`.
- To run the account tests: `python manage.py test apps.accounts`.

If you want stricter compatibility with Django's management commands (e.g., `createsuperuser`), we can make the model inherit from `AbstractBaseUser` and provide the necessary fields (e.g., `is_superuser`). For now, the model is intentionally minimal per your request.