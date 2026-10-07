from collections import Counter

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from cvat.apps.engine.models import LabeledShape, Task


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def annotation_counts(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    jobs = task.segment_set.values_list("job__id", flat=True)

    annotations = (
        LabeledShape.objects
        .filter(job_id__in=jobs)
        .select_related("label")
    )

    counts = Counter(annotation.label.name for annotation in annotations)

    return JsonResponse({
        "task_id": task.id,
        "total_annotations": sum(counts.values()),
        "counts": dict(sorted(counts.items())),
    })
