from django.db import models
from django.db.models.fields import CharField, URLField
from django.db.models.fields.files import ImageField

#los modelos se usan para cargar los datos al admin

class Project(models.Model):
    title = CharField(max_length=150)
    description= CharField(max_length=300)
    image = ImageField(upload_to="portfolio/images/")
    url= URLField(blank=True)
