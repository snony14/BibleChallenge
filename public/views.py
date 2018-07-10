from django.shortcuts import render
from django.http import HttpResponse

'''
This contains all website that are public to the users!!
'''

def home(request):
    return render(request, "public/home.html",dict())#HttpResponse("This is home", content_type="text/plain")

def search_team(request):
    #TODO should contain the join button!! but user must have logged in!!
    return HttpResponse("searching all team that are public")

def about(request):
    return HttpResponse("About us!")
