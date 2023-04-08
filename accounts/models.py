from django.db import models
from django.contrib.auth.models import AbstractUser

app_name = 'accounts'

# Create your models here.
class User(AbstractUser):
    phone_number = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=50, blank=True)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.username
    

    

