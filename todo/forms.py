from django import forms
from django.forms import ModelForm
from .models import Task

class TaskForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter your task'}))

    class Meta:
        model = Task
        fields = "__all__"