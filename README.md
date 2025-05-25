# djangoazurebatch
uv run manage.py shell -c "from core.models import TaskLog; print('ok')"
uv run manage.py makemigrations 
uv run manage.py migrate
uv run manage.py t1

uv run manage.py shell 
>>> from core.models import TaskLog
>>> TaskLog.objects.all().order_by('-start_time')