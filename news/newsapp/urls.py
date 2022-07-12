# I created this file
from django.urls import path

from . import views

app_name = 'newsapp'
urlpatterns = [
    #ex: /newsapp/
    path("", views.index, name="index"),
    #ex: /newsapp/1/
    path("<int:news_id>/", views.detail, name="detail"),
]