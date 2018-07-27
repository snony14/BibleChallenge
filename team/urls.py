from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('create', create_team, name="create_team"),
]
