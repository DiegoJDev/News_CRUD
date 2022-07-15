#I created form.py
from django import forms
from .models import News

#Here we got our form, form is same as class News because thanks to django this is super easy to do.
class NewsForm(forms.Form):
    class Meta:
        model = News
        fields = '__all__' # all fields because we want them to fill all fields.

        
