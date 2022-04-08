from django.contrib import admin
from .models import Project

#se registra el modelo para que se pueda visualizar 

admin.site.register(Project)
