"""
URL configuration for five project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# five/urls.py - The Project's main URL configuration file
from django.contrib import admin
from django.urls import path, include # <-- CRUCIAL: Must import 'include'

urlpatterns = [
    # Built-in path for the admin interface
    path('admin/', admin.site.urls),
    
    # Path to include URLs from your 'todo' application. 
    # This makes the task list the default homepage (path='')
    path('', include('todo.urls')), # <-- CRUCIAL: Links the root URL to your todo app
]