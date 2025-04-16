from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

User = get_user_model()

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Task(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    due_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    tags = models.ManyToManyField(Tag, blank=True)
    
    def __str__(self):
        return self.title

#class Notification(models.Model):
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    #task = models.ForeignKey(Task, on_delete=models.CASCADE)
    #message = models.TextField()
    #created_at = models.DateTimeField(auto_now_add=True)

    #def __str__(self):
        #return f"Notification for {self.user.username} - {self.task.title}"


admin_task = [
    Tag,
    Task,
    #Notification
]
