from django.contrib import admin
from django.urls import path, re_path
from .views import *


urlpatterns = [
    path('<int:book>/', getChapter,name="bible book"),
]
