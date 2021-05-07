from django import forms
from django.forms import ModelForm

from .models import *

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':"add new todo item"})
        }
