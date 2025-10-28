from django.test import TestCase

# Create your tests here.
from django.utils import timezone
from todo.models import Task # <-- Correct import using 'todo' app name

# Create dummy tasks for testing
def create_task(title, days=0, is_completed=False):
    """
    Helper function to create a Task with a due_date offset from now.
    """
    time = timezone.now() + timezone.timedelta(days=days)
    return Task.objects.create(title=title, due_date=time, is_completed=is_completed)

class TaskModelTests(TestCase):
    
    def test_was_created_successfully(self):
        """
        TDD Cycle 1: Verifies a task can be created and the title is stored correctly.
        """
        task = create_task("Test task title", days=1)
        # Check that the title matches what we input
        self.assertEqual(task.title, "Test task title")
        # Check that the completion status is the default (False)
        self.assertIs(task.is_completed, False)
    
    def test_complete_task_sets_to_true(self):
        """
        TDD Cycle 2 (Test 1 of 2): Verifies the custom 'complete_task' method works.
        """
        task = create_task("Task to complete")
        # Assert it's initially False
        self.assertIs(task.is_completed, False)
        
        task.complete_task()
        # Assert it's True after running the method
        self.assertIs(task.is_completed, True)
        
    def test_complete_task_only_saves_once(self):
        """
        TDD Cycle 2 (Test 2 of 2): Verifies completing an already completed task does nothing harmful.
        """
        task = create_task("Already completed task", is_completed=True)
        # Call the method again
        task.complete_task()
        # Ensure it remains True
        self.assertIs(task.is_completed, True)