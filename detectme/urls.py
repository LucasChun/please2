from django.conf.urls import url, include
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('detectme', views.detectme, name="detectme"),
    ]