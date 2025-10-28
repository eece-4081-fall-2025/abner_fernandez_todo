from django import forms
from todo.models import Task

class TaskForm(forms.ModelForm):
    """
    Form used to capture user input for creating a new Task object.
    """
    class Meta:
        model = Task
        fields = ['title', 'due_date']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Add a new task...'}),
            'due_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
