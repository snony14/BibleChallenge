from django.shortcuts import render, redirect

def create_challenge(request):
    #a post request
    return render(request,'challenge/create.html', dict())#redirect("/")

def post_comment(request):
    #a post request
    return redirect("/")

def delete_comment(request, id):
    #a put request
    return redirect("/")

from django.http import JsonResponse
def getBible(request):
    bible = open("bible_books.json", 'r')
    return JsonResponse(bible)
