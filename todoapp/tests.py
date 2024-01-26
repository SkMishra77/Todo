from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from .models import TaskModel


class TodoAPITestCase(TestCase):
    fixtures = ['todoapp/fixture/todo.json']

    def setUp(self):
        self.client = APIClient()
        self.data = {
            "email": "sanat123@example.com",
            "password": "12345678"
        }
        response = self.client.post('/api/user/login/', self.data, format='json')
        self.token = response.data['responseData']['token']['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

    def test_add_task(self):
        url = '/api/todo/addTask/'
        data = {
            "title": "TODO",
            "description": "Testing for todo",
            "due_date": "2024-02-01"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.data['error'], False)
        self.assertEqual(response.data['status_code'], status.HTTP_200_OK)
        self.assertIn('TaskId', response.data['responseData'])

    def test_update_todo(self):
        url = '/api/todo/updateTask/'
        data = {
            "title": "TODO Testing",
            'TaskId': 'Task_f2568a728548e1f64e75ed2702b907b7'

        }

        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.data['error'], False)
        self.assertEqual(response.data['status_code'], status.HTTP_200_OK)
        instance = TaskModel.objects.get(pk='Task_f2568a728548e1f64e75ed2702b907b7')
        self.assertEqual(instance.title, 'TODO Testing')

    def test_get_todo(self):
        url = '/api/todo/getTask/?task_id=Task_f2568a728548e1f64e75ed2702b907b7'
        response = self.client.get(url, format='json')
        self.assertEqual(response.data['error'], False)
        self.assertEqual(response.data['status_code'], status.HTTP_200_OK)

    def test_getall_todo(self):
        url = '/api/todo/getAllTasks/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.data['error'], False)
        self.assertEqual(response.data['status_code'], status.HTTP_200_OK)

    def test_delete_todo(self):
        url = '/api/todo/deleteTask/?task_id=Task_f2568a728548e1f64e75ed2702b907b7'
        response = self.client.delete(url, format='json')
        self.assertEqual(response.data['error'], False)
        self.assertEqual(response.data['status_code'], status.HTTP_200_OK)
