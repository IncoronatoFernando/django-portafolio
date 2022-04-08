from unicodedata import name
from django.shortcuts import render
from .models import Project

#con este funcion lo que se hace es crear la pagina de inicio

def home(request):
    projects= Project.objects.all()
    return render (request, 'index.html', {'projects':projects})
    
    
