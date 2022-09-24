from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin




class CustomUserManager(BaseUserManager):
    def create_superuser(self, email, password, **extra_fields):

        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(
            email, 
            password,
            **extra_fields,
            )
            
        user.is_superuser = True
        user.is_staff = True
        user.is_admin = True
        user.save()

        return user
        
    def create_user(self, email, password=None, **extra_fields):
        if email is None:
            raise TypeError('Users must have an email address.')

        user = self.model(
            email=self.normalize_email(email),
            **extra_fields
            )
        user.set_password(password)
        user.save()

        return user

    



# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):
    user_id =  models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=255, unique=True )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=15, null=True, blank=True)
    nationality = models.CharField(max_length=50, default="0")
    country = models.CharField(max_length=60, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=200, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(auto_now=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=True)
    
    objects = CustomUserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    class Meta:
        managed = True
        db_table = 'User'
    
    
    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name
        
    def __str__(self):
        return self.username

