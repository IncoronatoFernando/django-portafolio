from distutils.command.upload import upload
from email.mime import image
from django.db import models
import datetime


class Posts(models.Model):
    title= models.CharField( max_length=50)
    description=models.TextField()
    image= models.ImageField(upload_to='blog/images')
    date= models.DateField(datetime.date.today)
