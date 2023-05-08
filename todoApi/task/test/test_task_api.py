from rest_framework.test import APIClient
from rest_framework import status
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from task.serializers import TaskSerializer
from core.models import Task, Status

TASK_URL = reverse('task:task-list')

def get_url_detail(id):
    return reverse('task-detail', args=[id])

def create_task(user, **params):
    payload = {
        'title': 'Default Task Title',
        'description': 'Default Task Description'   
    }
    payload.update(params)
    default_status = {
        'statusname':'pending'
    }
    status = Status.objects.create(**default_status)

    task = Task.objects.create(owner=user, status=status, **payload)
    task.tags.set = []
    return task

class PublicTaskTest(TestCase):
    """Test get task unauthenticated"""
    def setUp(self):
        self.client = APIClient()

    def test_get_task_unauthenticated(self):
        """Test get task unauthenticated"""
        res = self.client.get('/api/tasks/')
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_create_task_unauth(self):
        payload = {
        'title': 'Default Task Title',
        'description': 'Default Task Description'
        }
        res = self.client.post('/api/tasks/', payload)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

class PrivateTaskTest(TestCase):
    """Test get task authenticated"""
    def setUp(self):
        self.client = APIClient()
        self.user_test = {
            'email': 'test@example.com',
            'password': 'testpass'
        }
        self.user = get_user_model().objects.create(**self.user_test)
        self.client.force_authenticate(self.user)
    
    def test_get_task_authenticated(self):
        create_task(user=self.user)
        create_task(user=self.user)
        res = self.client.get('/api/tasks/')
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 2)
    
    def test_get_detail_task(self):
        task = create_task(user=self.user)
        url = get_url_detail(task.id)
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        serializer = TaskSerializer(task)
        self.assertEqual(res.data, serializer.data)



    # def test_other_user_try_delete_task(self):
    #     self.other_user_detail = {
    #         'email': 'other@example.com',
    #         'password': 'otherpass'
    #     }
    #     self.other_user = get_user_model().objects.create(**self.other_user_detail)
    #     self.task = create_task(user=self.user)
    #     res = self.client.delete('/api/tasks')
