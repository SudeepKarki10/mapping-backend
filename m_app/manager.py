from django.contrib.auth.base_user import BaseUserManager
from django.db import models  # Add this import

class CustomUserManager(BaseUserManager):
    def create_user(self, phone_number,email, password, **extra_fields):
        if not phone_number:
            raise ValueError("Phone number is required!!")

        if not email:
            raise ValueError("Email is required!!")

        email = self.normalize_email(email)
        phone_number = self.normalize_phone_number(phone_number)

        user = self.model(
            phone_number=phone_number,
            email=email,
            **extra_fields
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,phone_number, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')
        return self.create_user(phone_number,email, password, **extra_fields)
       
    def normalize_phone_number(self, phone_number):
        # Normalize phone number, you might want to implement your own logic
        # to handle formatting or validation based on your specific needs
        return phone_number
