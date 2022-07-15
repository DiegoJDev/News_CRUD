
from django.urls import  reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic import CreateView, UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView


from .forms import NewsForm
from .models import News

# Create your views here.
#I worked with generic based-views bracuse it's less more efficient and a good practice.

#Index here, list of views.
class NewsList(ListView):
    template_name="newsapp/index.html" 
    context_object_name="list_news"

    def get_queryset(self):
        return News.objects.order_by("-update_date")#Put here how we want the list to show news, new ones to older ones



#Read: we can read the whole new beacuse of it.
class DetailNews(DetailView):
    template_name="newsapp/detail.html"
    model = News

#Create:Like we create an object here, we send de form, we created before.
class CreateNews(CreateView): 
    template_name="newsapp/create.html"
    model = News
    form = NewsForm
    fields = "__all__"
    success_url = reverse_lazy("newsapp:index")


#Update: You need to edit the new, then we need again our form with information we put before there.
class UpdateNews(UpdateView):
    template_name="newsapp/update.html"
    model = News
    forms= NewsForm
    fields = "__all__"
    success_url = reverse_lazy('newsapp:index')

#Delete: After deleted you are redirecting to the list of news.
class DeleteNews(DeleteView):
    template_name = 'newsapp/delete.html'
    model = News
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('newsapp:index')
