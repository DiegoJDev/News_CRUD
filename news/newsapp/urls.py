# I created this file
from django.urls import path
from django.views.generic import RedirectView

from .views import NewsList , DetailNews, CreateNews, UpdateNews, DeleteNews


app_name = 'newsapp'
#app_name in order to not hard coding.
urlpatterns = [

    path('', RedirectView.as_view(url='index/', permanent=True)),#I did RedirectView to link http://127.0.0.1:8000/ to http://127.0.0.1:8000/index/

    path("index/", NewsList.as_view(), name='index'),

    # got <int:pk> to let knowing which object sepecificly
    path("detail/<int:pk>", DetailNews.as_view(), name='detail'),

    path("create/", CreateNews.as_view(), name='create'),

    path("<int:pk>/update/" , UpdateNews.as_view(), name='update'),

    path("<int:pk>/delete/", DeleteNews.as_view(), name='delete')

    
]