from django.urls import reverse
from vocabulary_db.models import *

def models_in_header(request):
    models = [Word, Source, Author, TypeSource]
    return {
        "nav_models": [
            {
                "name" : Word._meta.verbose_name_plural,
                "url" : reverse('words'),
                "activation" : "words",
            },
            {
                "name" : Source._meta.verbose_name_plural,
                "url" : reverse('sources'),
                "activation" : "sources", 
            },
            {
                "name" : Author._meta.verbose_name_plural,
                "url" : reverse('authors'),
                "activation" : "authors", 
            },
            {
                "name" : TypeSource._meta.verbose_name_plural,
                "url" : reverse('types'),
                "activation" : "types", 
            },
        ]
    }