from django.db import models

class TaskLog(models.Model):
    job_id = models.CharField(max_length=100)
    task_name = models.CharField(max_length=50)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.task_name} ({self.job_id})"
