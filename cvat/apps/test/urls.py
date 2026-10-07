from django.urls import path

from .views import annotation_counts


urlpatterns = [
    path(
        "tasks/<int:task_id>/annotation-counts/",
        annotation_counts,
        name="annotation-counts",
    ),
]
