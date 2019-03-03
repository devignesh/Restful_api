from django.contrib import admin
from .models import Language, Paradigm, Programmer

# Register your models here.

admin.site.register(Language)
admin.site.register(Paradigm)
admin.site.register(Programmer)