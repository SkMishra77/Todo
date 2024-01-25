from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.db import models


#  Custom User Manager

class UserManager(BaseUserManager):
    def create_user(self, email, name, password=None,
                    password2=None, **extra_fields):
        """
        Creates and saves a User with the given email, username, name and password.
        """
        if not email:
            raise ValueError('User must have an email')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user


#  Custom User Model
class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, primary_key=True)
    name = models.CharField(max_length=64)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email
