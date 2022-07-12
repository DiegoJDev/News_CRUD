from django.contrib import admin
from .models import News

# Register your models here.

# Aca importo el model News para que se pueda editar en el administrador

admin.site.register(News)

