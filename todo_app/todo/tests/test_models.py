import pytest
from django.test import TestCase
from mixer.backend.django import mixer

from todo_app.todo.models import Task

pytestmark = pytest.mark.django_db

class TaskTests(TestCase):
    def test_create(self):
        mixer.blend(Task)
        assert Task.objects.count() == 1

    def test_query(self):
        expected = mixer.blend(Task, title="task1")
        t = Task.objects.get(title__exact="task1")
        assert t == expected
