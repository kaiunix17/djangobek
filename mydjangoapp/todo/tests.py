from django.test import TestCase
from .models import Task

class TaskModelTest(TestCase):
    def test_str_representation(self):
        task = Task(title="Test Task")
        self.assertEqual(str(task), task.title)