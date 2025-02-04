from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Task, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    #assigned_to = UserSerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = '__all__'

#class NotificationSerializer(serializers.ModelSerializer):
    #class Meta:
        #model = Notification
        #fields = '__all__'
