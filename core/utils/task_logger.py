from core.models import TaskLog
from datetime import datetime
from django.utils import timezone

def run_task(task_name, job_id, logic_fn):
    log = TaskLog.objects.create(task_name=task_name, job_id=job_id)
    try:
        logic_fn()
    finally:
        log.end_time = timezone.make_aware(datetime.now(), timezone.get_current_timezone())
        log.save()
