"""Модели приложения TasksApp."""

from django.db import models


# Create your models here.

class Task(models.Model):
    """Модель задания."""

    summary = models.CharField(verbose_name='Краткое описание', max_length=128)
    description = models.TextField(verbose_name='Описание')
    date_of_issue = models.DateField(verbose_name='Дата назначения', auto_now_add=True)
    assigned_by = models.ForeignKey(to='users_app.User', verbose_name='Кто назначил', on_delete=models.CASCADE,
                                    related_name='tasks_assigned')
    assigned_to = models.ForeignKey(to='users_app.User', verbose_name='Кому назначено', on_delete=models.CASCADE,
                                    related_name='tasks_taken')
    done = models.BooleanField(verbose_name='Выполнено', default=False)
    dead_line = models.DateField(verbose_name='Срок исполнения', null=True, blank=True)
    comment = models.TextField(verbose_name='Комментарий', null=True, blank=True)

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'

    def __str__(self):
        return f'{self.summary}, для {self.assigned_to.last_name} {self.assigned_to.first_name}'