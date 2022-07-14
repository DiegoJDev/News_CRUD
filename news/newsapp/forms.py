from pyexpat import model
from django import forms
from .models import News

#Como se quiere llenar la misma informacion de un modelo hacemos un classModelForm
class NewsForm(forms.Form):
    class Meta:
        model = News
        fields = '__all__' #Queremos que se llenen todos los atributos del model

        
