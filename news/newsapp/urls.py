# I created this file
from django.urls import path

from .views import NewsList , DetailNews, CreateNews, UpdateNews, DeleteNews
from django.views.generic import RedirectView

app_name = 'newsapp'
urlpatterns = [

    path('', RedirectView.as_view(url='index/', permanent=True)),

    path("index/", NewsList.as_view(), name='index'),

    path("detail/<int:pk>", DetailNews.as_view(), name='detail'),

    path("create/", CreateNews.as_view(), name='create'),

    path("<int:pk>/update/" , UpdateNews.as_view(), name='update'),

    path("<int:pk>/delete/", DeleteNews.as_view(), name='delete')

    
]