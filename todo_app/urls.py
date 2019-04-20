from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter

from todo_app.todo.views import TaskViewSet

router = DefaultRouter()
router.register(r"todo", TaskViewSet)

urlpatterns = [
    url(r"^api/", include((router.urls, "todo"))),
]
