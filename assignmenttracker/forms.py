from django import forms
from .models import Task
from django.forms.widgets import DateInput  # Import the DateInput widget
# class TaskForm(forms.ModelForm):
#     class Meta:
#         model = Task
#         fields = ['subject', 'title', 'description', 'due_date', 'priority', 'status']
#


class TaskForm(forms.ModelForm):
    class Meta:

        model = Task
        fields = ['subject', 'title', 'description', 'due_date', 'priority', 'status']

