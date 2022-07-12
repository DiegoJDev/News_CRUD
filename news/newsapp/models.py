from django.db import models
from django.utils import timezone

# Create your models here.

class News(models.Model):
    #el id se pone automaticamente gracias a django
    news_text = models.TextField #comprobar si se pueden usar mas de 250 letras o caraceres poeque si no se debe añadir el max lenght
    pub_date = models.DateField(default=timezone.now)
    author=models.CharField

