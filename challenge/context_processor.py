from django.conf import settings
import json

def global_settings(request):
    # return any necessary values
    bible = open("challenge/bible_books.json", 'r')
    json_file = bible
    bible = json.load(bible)#[0]
    keys = bible.keys()
    return {
        'bible':bible,
        'keys' : keys,
    }
