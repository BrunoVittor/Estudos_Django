from django.forms import ModelForm
from .models import Client

class PersonForm(ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'age', 'sex']
