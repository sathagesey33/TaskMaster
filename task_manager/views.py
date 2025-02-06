from django.contrib.auth.models import User
from django.utils import timezone
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from .models import Task, Tag
from .serializers import TaskSerializer, TagSerializer

class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        serializer.save(assigned_to=self.request.user)

class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
permission_classes = [AllowAny]

class TagListCreateView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAuthenticated]

#class NotificationListView(generics.ListAPIView):
    #serializer_class = NotificationSerializer
    #permission_classes = [permissions.IsAuthenticated]

    #def get_queryset(self):
        #return Notification.objects.filter(user=self.request.user)

class TaskProgressUpdateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, task_id):
        try:
            task = Task.objects.get(id=task_id)
            new_status = request.data.get('status')

            if new_status not in dict(Task.STATUS_CHOICES):
                return Response({"error": "Invalid status"}, status=400)

            task.status = new_status
            task.updated_at = timezone.now()
            task.save()

            return Response({"message": "Task status updated", "task": TaskSerializer(task).data})
        except Task.DoesNotExist:
            return Response({"error": "Task not found"}, status=404)



