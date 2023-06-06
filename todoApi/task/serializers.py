from rest_framework import serializers
from core.models import Task, Tag, Status


class TaskSerializer(serializers.ModelSerializer):
    status = serializers.SlugRelatedField(
        queryset=Status.objects.all(),
        slug_field='statusname'
    )
    tags = serializers.SlugRelatedField(
        many=True,
        queryset=Tag.objects.all(),
        slug_field="tagname",   
    )
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'tags', 'status']
        read_only = ['id']

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ['id', 'statusname']
        read_only = ['id']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'tagname']
        read_only = ['id']