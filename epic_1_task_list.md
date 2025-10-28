Epic 1: Task Management (Core Functionality) - Development Tasks

This list breaks down the User Stories for the core ToDo functionality into small, executable development tasks, forming the work required for the Minimum Viable Product (MVP).

User Story ID

User Story Title

Development Tasks

Status

US 1

As a User, I want to quickly add a new task...

1. Define Task model with title, is_completed, and due_date fields.

DONE (TDD Cycle 1)





2. Create Django TaskForm using the Task model.







3. Implement task creation logic in task_list view (handle POST).



US 2

As a User, I want to view a list of all my pending tasks...

4. Implement task_list view to query incomplete tasks.







5. Create task_list.html template structure and render incomplete list.



US 3

As a User, I want to mark a task as complete...

6. Implement complete_task() method on the Task model.

DONE (TDD Cycle 2)





7. Implement task_complete view to call the complete_task method.







8. Add "Complete" button/link to each task in the template.



US 5

As a User, I want to delete a task entirely...

9. Implement task_delete view.







10. Add "Delete" button/link to tasks in the template.



US 6

As a User, I want to see a running count of incomplete tasks...

11. Calculate task_count (incomplete tasks count) in task_list view context.







12. Display task_count prominently in the task_list.html template.



US 7

As a User, I want to view an archive of my completed tasks...

13. Query and pass completed_tasks list to the task_list view context.







14. Render a separate "Archive" section for completed tasks in the template.



Completed TDD Evidence (Push 1 & 2)

Cycle

Description

Files Committed

Cycle 1 (Push 1)

Implement and test the core Task model structure.

models.py, tests.py

Cycle 2 (Push 2)

Implement and test the complete_task() method.

models.py, tests.py