from django.db import models

# Create your models here.
from django.utils import timezone # Required for the default value of due_date

class Task(models.Model):
    """
    Represents a single ToDo task.
    """
    # US 1: Must have a title to be added.
    title = models.CharField(max_length=200) 
    
    # US 3: Tracks completion status, defaults to incomplete.
    is_completed = models.BooleanField(default=False) 
    
    # US 1: Allows setting a due date, defaults to the current time.
    due_date = models.DateTimeField('due date', default=timezone.now) 
    
    # Timestamp for when the task was created (automatic)
    created_at = models.DateTimeField(auto_now_add=True) 

    def complete_task(self):
        """
        Marks the task as completed by setting is_completed to True.
        This method was developed during TDD Cycle 2 (US 3).
        """
        if not self.is_completed:
            self.is_completed = True
            self.save()

    def __str__(self):
        """Returns the task title as the string representation."""
        return self.title

    class Meta:
        # Orders tasks by due date by default
        ordering = ['due_date']
