# from rest_framework.test import APIClient

# from django.test import TestCase
# from django.contrib.auth import get_user_model

# from task import serializers

# class PublicTaskTest(TestCase):


#     def create_task(self, **params):
#         default = {
            
#         }


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
