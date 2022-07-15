from django.contrib import admin
from .models import News

# Register your models here.

# I got to import model News in order to admin could work on it.

admin.site.register(News)

