from django.contrib import admin

# Register your models here.

from applications.films.models import Films
admin.site.register(Films)
