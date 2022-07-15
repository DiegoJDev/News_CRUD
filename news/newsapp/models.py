from django.db import models
from django.utils import timezone

# Create your models here.

class News(models.Model):
    #el id se pone automaticamente gracias a django
    title = models.CharField(max_length=100, default="Noticia")
    news_text = models.TextField (max_length=10000, default="Noticia") #comprobar si se pueden usar mas de 250 letras o caraceres poeque si no se debe añadir el max lenght
    author = models.CharField(max_length=50, default="Anonimo")
    pub_date = models.DateField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return ("Titulo:" + self.title
        + "\n Noticia:" + self.news_text
        +"\n Autor:" + self.author
        + "\n fecha de publicacion:" + str(self.pub_date) )

