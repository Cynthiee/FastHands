from django.db import models
from django.contrib.auth.models import AbstractUser

class Users(AbstractUser):
    nin = models.IntegerField(unique=True)
    
    def __str__(self):
        return self.username


