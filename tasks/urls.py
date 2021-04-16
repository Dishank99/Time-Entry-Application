from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home-screen'),
    path('add/', AddTask.as_view(), name='add-task-screen'),
    path('update/<int:pk>', UpdateTask.as_view(), name='update-task-screen'),
]