from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class MyAccountManager(BaseUserManager):
    """Custom user account manager"""

    def create_user(self, first_name, last_name, user_name, email, password=None):
        if not email:
            raise ValueError("User must have an email address")
        if not user_name:
            raise ValueError('User must have a user name')

        user = self.model(
            email = self.normalize_email(email),
            user_name = user_name,
            first_name = first_name,
            last_name = last_name,
        )
        user.set_password = password
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, user_name, email, password=None):
        """Create superuser"""
        user = self.create_user(
            first_name = first_name,
            last_name = last_name,
            user_name = user_name,
            email = self.normalize_email(email),
            password=password)
        user.is_admin = True
        user.is_staff = True
        user.is_superadmin =True
        user.save(using=self._db)

        return user

class Account(AbstractBaseUser):
    """Custom user model"""
    first_name      = models.CharField(max_length=50)
    last_name       = models.CharField(max_length=50)
    user_name       = models.CharField(max_length=50, unique=True)
    email           = models.EmailField(max_length=100, unique=True)
    phone_number    = models.CharField(max_length=50)

# mandatory
    date_joined     = models.DateField(auto_now_add=True)
    last_login      = models.DateField(auto_now_add=True)
    is_admin        = models.BooleanField(default=False)
    is_active       = models.BooleanField(default=True)
    is_staff        = models.BooleanField(default=False)
    is_superadmin   = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'first_name', 'last_name']

    object = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, permission, object=None):
        return self.is_admin

    def  has_module_perm(self, add_label):
        return True
