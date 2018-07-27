from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('', profile, name="account"),
    path('challenges', challenges, name="challenges"),
    path('logout', logout_user, name="logout"),
    path('teams', teams, name="teams"),
    path('settings', settings, name="settings"),
]
