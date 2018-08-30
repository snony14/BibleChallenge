from django.conf import settings
import json
import os
from glob import glob

def global_settings(request):
    default = "kjv"
    # return any necessary values
    #bible_pos = open("challenge/bib_pos.json", 'r')
    directories_path = glob("bible_json/kjv/*")
    directories = [foo(dirPath) for dirPath in directories_path]
    directories.sort(key=getKey)
    return {
        'directories':directories
    }


def foo(file):
    book_pos = file.split("/")[-1].split("_")
    pos = int(book_pos[0])
    book = " ".join(book_pos[1:])
    return (pos, book)

def getKey(item):
    return item[0]
