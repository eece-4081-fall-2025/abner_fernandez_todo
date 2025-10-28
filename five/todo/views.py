
# Create your views here.
# five/todo/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from todo.models import Task
from todo.forms import TaskForm
from django.utils import timezone

def task_list(request):
    """
    Handles displaying the list of tasks (US 2) and creating new tasks (US 1).
    """
    # Create a new Task when the user submits the form
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            # Save the task to the database
            form.save()
            return redirect('todo:task_list')
    
    # Otherwise, prepare to display the list and the empty form
    else:
        # Create a new form instance for the task creation box
        form = TaskForm(initial={'due_date': timezone.now().strftime('%Y-%m-%dT%H:%M')})
        
    # Retrieve all tasks, ordered by due date, for display
    tasks = Task.objects.all().order_by('due_date')

    context = {
        'tasks': tasks,
        'form': form,
    }
    return render(request, 'todo/task_list.html', context)

@require_POST
def complete_task(request, pk):
    """
    Marks a task as completed using the custom complete_task method (US 3).
    Only allows POST requests to prevent accidental completion via browser link.
    """
    task = get_object_or_404(Task, pk=pk)
    task.complete_task() # Calls the model method verified by TDD Cycle 2
    return redirect('todo:task_list')

@require_POST
def delete_task(request, pk):
    """
    Deletes a task (US 4).
    Only allows POST requests.
    """
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('todo:task_list')
