from django.db import models

# Create your models here.
class User(models.Model):
    username= models.CharField(max_length=30)
    password = models.CharField(max_length=10)

class Picture(models.Model):
    poster = models.ForeignKey(User,on_delete=models.CASCADE)
    text = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='images',null=True,blank=True)