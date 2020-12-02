from django.db import models
from django.contrib.auth.models import User, AbstractUser   
from django.db.models.signals import post_save
from django.dispatch import receiver



class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    adress = models.CharField(max_length=80, blank=True)
    phone = models.CharField(max_length=12, blank=True)
    ci = models.CharField(max_length=6, blank=True)
   

def __str__(self):
    return self.user



class Usuario_Extension(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rut = models.CharField(max_length=10, blank=True)
    dv = models.CharField(max_length=1, blank=True)



