from django.db import models

# Create your models here.
class SuperUser(models.Model):
    first_name = models.CharField(max_length=50, blank=True, null=True)
    Last_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField( max_length=254, unique=True)
    phoneNumber = models.CharField(max_length=50, blank=True, null=True)