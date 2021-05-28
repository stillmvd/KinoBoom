"""KinoBoom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/"""

from django.urls import include, path
from django.conf import settings 
from django.urls import path, include 
from django.conf.urls.static import static 

urlpatterns = [
    path('', 
        include('main.urls')),
]
    
if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

