from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Author)
admin.site.register(TypeSource)
admin.site.register(Source)
admin.site.register(Word)