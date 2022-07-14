# I created this file
from django.urls import path

from .views import NewsList , DetailNews, CreateNews, UpdateNews, DeleteNews

app_name = 'newsapp'
urlpatterns = [
    #ex: /newsapp/
    path("newsapp/", NewsList.as_view(), name='index'),

    path("detail/<int:pk>", DetailNews.as_view(), name='detail'),

    path("create/", CreateNews.as_view(), name='create'),

    path("<int:pk>/update/" , UpdateNews.as_view(), name='update'),

    path("<int:pk>/delete/", DeleteNews.as_view(), name='delete')

    
]