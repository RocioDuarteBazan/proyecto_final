from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    foto = models.ImageField(upload_to='usuarios', null=True)


    


