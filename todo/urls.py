from django.urls import path
from . import views
from .views import HomeView, index, updateTask, deleteTask, todo_list 


urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),

    path('list/', index, name='list'),
    path('update_task/<str:pk>/', updateTask, name="update_task"),
    path('list/', todo_list, name='todo_list'),
    path('delete/<str:pk>/', deleteTask, name="delete"),
]

