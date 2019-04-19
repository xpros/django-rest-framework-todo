from mixer.backend.django import mixer
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from todo_app.todo.models import Task

TASK = {
    "title": "A test task",
    "description": "Testing the creation of a task",
    "status": "todo"
}


class TaskViewSetTest(APITestCase):
    def test_create_task(self):
        url = reverse("todo:task-list")
        response = self.client.post(url, TASK, format="json")
        assert response.status_code == status.HTTP_201_CREATED
        assert Task.objects.count() == 1
        assert Task.objects.get().title == "A test task"

    def test_read_task(self):
        task = mixer.blend(Task)
        url = reverse("todo:task-detail", kwargs={"pk": task.pk})
        response = self.client.get(url, format="json")
        assert response.status_code == status.HTTP_200_OK
        assert response.data["title"] == task.title

    def test_update_task(self):
        task = mixer.blend(Task)
        url = reverse("todo:task-detail", kwargs={"pk": task.pk})
        data = {"status": "wip"}
        response = self.client.patch(url, data, format="json")
        assert response.status_code == status.HTTP_200_OK
        assert Task.objects.get().status == "wip"

    def test_delete_task(self):
        mixer.cycle(2).blend(Task)
        task = mixer.blend(Task)
        url = reverse("todo:task-detail", kwargs={"pk": task.pk})
        assert Task.objects.count() == 3
        response = self.client.delete(url, format="json")
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert Task.objects.count() == 2
