from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.TaskListAPIView.as_view(), name='task-list'),
    path('tasks/<int:pk>/', views.TaskRetrieveUpdateDestroyAPIView.as_view(), name='task-detail'),

]
