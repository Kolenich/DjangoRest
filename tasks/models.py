"""Модели приложения TasksApp."""

from django.db import models


# Create your models here.

class Task(models.Model):
    """Модель задания."""

    summary = models.CharField('Краткое описание', max_length=128)

    description = models.TextField('Описание')
    comment = models.TextField('Комментарий', null=True, blank=True)

    date_of_issue = models.DateTimeField('Дата назначения', auto_now_add=True)
    dead_line = models.DateTimeField('Срок исполнения')

    done = models.BooleanField('Выполнено', default=False)
    archived = models.BooleanField('В архиве', default=False)

    assigned_by = models.ForeignKey('auth.User', models.CASCADE, verbose_name='Кто назначил',
                                    related_name='tasks_assigned')
    assigned_to = models.ForeignKey('auth.User', models.CASCADE, verbose_name='Кому назначено',
                                    related_name='tasks_taken')

    attachment = models.OneToOneField('common_models.Attachment', models.CASCADE, verbose_name='Вложение к заданию',
                                      null=True, blank=True)

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'
        db_table = 'tasks'

    def __str__(self):
        return f'{self.summary}, для {self.assigned_to.last_name} {self.assigned_to.first_name}'
