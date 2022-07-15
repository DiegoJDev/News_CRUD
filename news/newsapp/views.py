from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, DetailView
from django.views.generic import CreateView, UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView


from .forms import NewsForm
from .models import News

# Create your views here.


class NewsList(ListView):
    template_name="newsapp/index.html" 
    context_object_name="list_news"

    def get_queryset(self):
        return News.objects.order_by("-update_date")




class DetailNews(DetailView):
    template_name="newsapp/detail.html"
    model = News


class CreateNews(CreateView): 
    template_name="newsapp/create.html"
    model = News
    form = NewsForm
    fields = "__all__"
    success_url = reverse_lazy("newsapp:index")



class UpdateNews(UpdateView):
    template_name="newsapp/update.html"
    model = News
    forms= NewsForm
    fields = "__all__"
    success_url = reverse_lazy('newsapp:index')


class DeleteNews(DeleteView):
    template_name = 'newsapp/delete.html'
    model = News
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('newsapp:index')
