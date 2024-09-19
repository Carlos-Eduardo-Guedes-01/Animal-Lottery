from celery import Celery
from celery.schedules import crontab
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('seu_projeto')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# Configuração do Celery Beat
app.conf.beat_schedule = {
    'cadastra-aposta-diaria': {
        'task': 'loteria.tasks.cadastra_aposta_task',
        'schedule': crontab(hour=18, minute=0),  # Executa todos os dias às 18:00
    },
}