from django.forms import ModelForm
from .models import Eating

class EatingForm(ModelForm):
    class Meta:
        model = Eating
        fields = ['date', 'meal']