from django.test import TestCase

from rest_framework import status
from rest_framework.test import APITestCase

from todo_api.models import ToDo

# Create your tests here.
class ToDoTestCase(APITestCase):
    def setUp(self):
        ToDo.objects.create(description="Write test cases")
        ToDo.objects.create(description="Add dummy task")
        ToDo.objects.create(description="Finish all testing")

    def test_create_todo(self):
        data = {"description":"Test the API"}
        response = self.client.post('/todos', data)
        expected_status = status.HTTP_201_CREATED
        self.assertEqual(response.status_code, expected_status)
    
    def test_create_empty_todo(self):
        data ={}
        response = self.client.post('/todos', data)
        expected_status = status.HTTP_400_BAD_REQUEST
        self.assertEqual(response.status_code, expected_status)

    def test_get_all_to_dos(self):
        response = self.client.get('/todos')
        self.assertEqual(len(response.data), 3)
        
    
    # def test_edit_todo(self):
    #     pass

    # def test_delete_todo(self):
