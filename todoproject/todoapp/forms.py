from django import forms
from . models import Task
class todoform(forms.ModelForm):
    class Meta:
        model=Task
        fields=['a','b','c']