# accounts/authentication_backends.py

from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

class CustomUserBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()

        # Check if the provided username is an email or username or phone number
        user = None
        if '@' in username:
            user = UserModel.objects.filter(email=username).first()
        elif UserModel.USERNAME_FIELD == 'username':
            user = UserModel.objects.filter(username=username).first()
        elif UserModel.USERNAME_FIELD == 'phone_number':
            user = UserModel.objects.filter(phone_number=username).first()

        if user and user.check_password(password):
            return user
