from django.db import models


# Create your models here.

class UserInfo(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.CharField(unique=True, max_length=16, null=False)
    pwd = models.CharField(max_length=16, null=False)
    email = models.EmailField(null=True)
    phone = models.BigIntegerField(null=False, default=110)


"""
class City(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True,null=False,max_length=16)
"""
