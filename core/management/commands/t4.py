import os
import time
from django.core.management.base import BaseCommand
from core.utils.task_logger import run_task

class Command(BaseCommand):
    help = 'Run task T4'

    def handle(self, *args, **kwargs):
        job_id = os.environ.get("AZ_BATCH_JOB_ID", "local-job")
        run_task("T4", job_id, self.execute_logic)

    def execute_logic(self):
        time.sleep(5)
