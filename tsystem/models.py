from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Ticket(models.Model):

    Priority = (
        ('Приоритет 1', 'Приоритет 1'),
        ('Приоритет 2', 'Приоритет 2'),
        ('Приоритет 3', 'Приоритет 3')
    )

    Status = (
        ('Ожидает','Ожидает'),
        ('В процессе','В процессе'),
        ('Фидбэк', 'Фидбэк'),
        ('Закрыт','Закрыт')
    )

    title = models.TextField('Название тикета', blank=True, null=True)
    description = models.TextField('Описание тикета', blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')  
    priority = models.CharField('Приоритет', choices=Priority, blank=True, max_length=50, default="Обычный")
    status = models.CharField('Статус', choices=Status, blank=True, max_length=50, default="Ожидает")
    date_create = models.DateTimeField('Дата создания', blank=True, null=True, default=datetime.now())
    executor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Исполнитель', related_name='executed_tasks')