from django.db import models
from django.contrib.auth.models import User

class Donors(models.Model):
     photo = models.ImageField(upload_to='profile_pic', default='default.jpg')
     name=models.CharField(max_length=30)
     email=models.CharField(max_length=40)
     bloodgroup=models.CharField(max_length=30)
     age=models.IntegerField()
     number=models.CharField(max_length=12)
     password=models.CharField(max_length=20)
     village=models.CharField(max_length=30)
     mandal=models.CharField(max_length=30)
     pincode=models.IntegerField()
     status=models.CharField(max_length=10,default="False")
     class Meta:
          db_table = 'blooddonation_donors'

