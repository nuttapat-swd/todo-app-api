from rest_framework.test import APIClient
from rest_framework import status

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from task import serializers
from core.models import Task

TASK_URL = reverse('task:task-list')

def create_task(user, **params):
    """Create and retuen a new task"""
    default_task = {
        'title': 'Test Task',
        'description': 'Test Task Description',
    }
    default_task.update(params)

    task = Task.objects.create(owner=user, **default_task)
    return task


class PublicTaskTest(TestCase):
    """Test unauthenticated get task list"""
    def setUp(self):
        self.client = APIClient()

    def test_auth_required(self):
        res = self.client.get(TASK_URL)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)



#     def test_create_task_by_serialization(self):
#         """Test creating a new task"""
#         payload = {
#             'title': 'Test task',
#             'description': 'Test task description'
#         }
#         serializers = serializers.TaskSerializer(payload)
#         if serializers.is_valid():
#             serializers.save()
#         self.assertEqual(serializers.data, payload)

    # def test_unauthenticated_create_task(self):
    #     """Test creating a new task"""
    #     payload = {
    #         'title': 'Test task',
    #         'description': 'Test task description'
    #     }
    #     res = self.client.post(
    #         '/api/tasks/',
    #         payload
    #     )
