from django.forms import ModelForm
from .models import BB

class BBForm(ModelForm):
    class Meta:
        model = BB
        fields = ('name', 'description', 'price', 'classification')
