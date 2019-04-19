from django.test import TestCase

from todo_app.todo.serializers import TaskSerializer
from mixer.backend.django import mixer


class TaskSerializerTests(TestCase):
    def test_serialize(self):
        task = mixer.blend("todo.Task")
        serializer = TaskSerializer(task)
        assert serializer.data["title"] == task.title
        assert serializer.data["description"] == task.description

    def test_deserialize_invalid(self):
        serializer = TaskSerializer(data={"task_id": None, "title": "wrong task id"})
        assert serializer.is_valid() is False
