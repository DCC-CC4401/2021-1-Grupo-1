from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.urls import reverse


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifier for
    authentication instead of AbstractUser's default username field.
    """

    def create_user(self, email, password, **extra_fields):
        """
        Create and save an user with the given email and password.
        """
        if not email:
            raise ValueError('The email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a superuser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')
        extra_fields['first_name'] = 'admin'
        extra_fields['last_name'] = ''
        extra_fields['phone_number'] = ''
        extra_fields['address'] = ''
        extra_fields['region'] = Region.objects.get(pk=1)
        extra_fields['comuna'] = Comuna.objects.get(pk=1)
        extra_fields['birth_date'] = None
        return self.create_user(email, password, **extra_fields)


class Region(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Comuna(models.Model):
    name = models.CharField(max_length=30)
    region = models.ForeignKey(Region, on_delete=models.PROTECT, null=False)

    def __str__(self):
        return self.name


class User(AbstractUser):
    username = None  # Not using AbstractUser's username field
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    email = models.EmailField(unique=True, blank=False)
    phone_number = models.CharField(max_length=12, blank=False)
    address = models.CharField(max_length=100, blank=False)
    region = models.ForeignKey(Region, on_delete=models.PROTECT, blank=False)
    comuna = models.ForeignKey(Comuna, on_delete=models.PROTECT, blank=False)
    description = models.CharField(max_length=260, blank=True)
    register_date = models.DateField(auto_now_add=True)
    birth_date = models.DateField(null=True, blank=False)  # Null for superuser

    USERNAME_FIELD = 'email'  # Use 'email' field for authentication
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return reverse('profile', kwargs={'user_id': self.id})
