from django.shortcuts import render
from django.http import HttpResponse

from glob import glob
# Create your views here.
def getChapter(request, book=0):
    #open the book
    book = 0 if book <0 or book >65 else book
    path = getBook(book) +"/*.json"
    ttl_chapters = len(glob(path))
    #print(ttl_chapters)
    return HttpResponse(ttl_chapters)


#TODO need a function that just grab the data from a particular
def getBook(numb):
    directories_path = glob("bible_json/kjv/*")
    directories = [foo(dirPath) for dirPath in directories_path]
    dir = dict(directories)
    return dir[numb]


#TODO: refactor the code
def foo(file):
    book_pos = file.split("/")[-1].split("_")
    pos = int(book_pos[0])
    book = " ".join(book_pos[1:])
    return (pos, file)
