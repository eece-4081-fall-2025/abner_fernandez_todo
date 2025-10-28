# five/todo/urls.py
from django.urls import path
from . import views

# Set the app_name so we can reference URLs easily in templates (e.g., 'todo:complete')
app_name = 'todo'
urlpatterns = [
    # path('', views.task_list, name='task_list') is the main list view (US 2 & 1)
    path('', views.task_list, name='task_list'),
    
    # path('complete/<int:pk>/', views.complete_task, name='complete') handles marking a task as done (US 3)
    path('complete/<int:pk>/', views.complete_task, name='complete'),
    
    # path('delete/<int:pk>/', views.delete_task, name='delete') handles removing tasks (US 4)
    path('delete/<int:pk>/', views.delete_task, name='delete'),
]