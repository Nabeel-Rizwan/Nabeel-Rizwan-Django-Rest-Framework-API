from django.contrib import admin
from django.urls import path, include
from .views import UserViewSet
from rest_framework import routers

router=routers.DefaultRouter()

router.register(r'User', UserViewSet)

urlpatterns = [    
    path('',include(router.urls))       ##  Automatic routing, assigns urls and displays endpoints through rest_framework
]
