from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from portfolio import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name="home"),
]
