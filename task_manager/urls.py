from django.urls import path
from .views import task_list_view, task_detail

urlpatterns = [
    path('list/', task_list_view, name="task-list"),
    path("list/<int:task_id>/", task_detail, name="task-detail"),
]
