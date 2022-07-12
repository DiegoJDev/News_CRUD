from hashlib import new
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import News

# Create your views here.

def index(request):
    latest_news_list=News.objects.all()
    return render (request, "newsapp/index.html", {
        "latest_news_list": latest_news_list
    })


def detail(request,news_id):
    news = get_object_or_404(News , pk=news_id)
    return render (request, "newsapp/detail.html",{
        "news": news
    })





