from django.urls import path
from .views import TaskListCreateView, TaskDetailView, TagListCreateView, TaskProgressUpdateView

urlpatterns = [
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('tasks/<int:task_id>/progress/', TaskProgressUpdateView.as_view(), name='task-progress-update'),
    path('tags/', TagListCreateView.as_view(), name='tag-list-create'),
    #path('notifications/', NotificationListView.as_view(), name='notification-list'),
]
