from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('create/', views.todo_create, name='todo_create'),
    path('<int:pk>/complete/', views.todo_complete, name='todo_complete'),
    path('<int:pk>/delete/', views.todo_delete, name='todo_delete'),
]
