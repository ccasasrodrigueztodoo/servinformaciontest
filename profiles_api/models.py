from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

class UserProfileManager(BaseUserManager):
    """Manager by user profiles"""
    def create_user(
        self, email, first_name, last_name, address, city, password=None
    ):
        """Create new user profile"""
        if not first_name:
            raise ValueError('El usuario debe tener un nombre')
        user = self.model(email=email, first_name=first_name, last_name=last_name, address=address, city=city)
        
        user.set_password(password)
        user.save(using=self._db)
        
        return user

    def create_superuser(
        self, email,first_name, last_name, address, city, password  
    ):
        """Create new superuser profile"""
        user = self.create_user(email,first_name, last_name, address, city, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        
        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """model by user in database"""
    #email = models.EmailField(max_length=225)
    email = models.EmailField(
        max_length=254, unique=True)
    first_name = models.CharField(
        max_length=50)
    last_name = models.CharField(
        max_length=50)
    address = models.CharField(
        max_length=50)
    city = latitude = models.CharField(
        max_length=50)   
    latitude = models.CharField(
        max_length=50)
    longitude = models.CharField(
        max_length=50)
    is_staff = models.BooleanField(
        default=False)
    objects = UserProfileManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name', 'address', 'city']

    def __str__(self):
        return self.first_name




