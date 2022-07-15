from django.db import models
from django.utils import timezone

# Create your models here.

#Thhe model is the first part of the MTV, so when made this class we can make migration to create our database.
class News(models.Model):
    #Id puts itself thanks to django
    title = models.CharField(max_length=100, default="Noticia")
    news_text = models.TextField (max_length=10000, default="Noticia") #At the beginning I got here CharField, but I changed it to TextField because news is a text.
    author = models.CharField(max_length=50, default="Anonimo")
    pub_date = models.DateField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    
    # A method to say how we want to be showed data.
    def __str__(self):
        return ("Titulo:" + self.title
        + "\n Noticia:" + self.news_text
        +"\n Autor:" + self.author
        + "\n fecha de publicacion:" + str(self.pub_date) )

