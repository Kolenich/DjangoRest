"""Модели приложения TasksApp."""

from django.db import models


# Create your models here.

class Task(models.Model):
    """Модель задания."""

    summary = models.CharField('Краткое описание', max_length=128)

    description = models.TextField('Описание')
    comment = models.TextField('Комментарий', null=True, blank=True)

    date_of_issue = models.DateTimeField('Дата назначения', auto_now_add=True)
    dead_line = models.DateTimeField('Срок исполнения', null=True, blank=True)

    done = models.BooleanField('Выполнено', default=False)
    archived = models.BooleanField('В архиве', default=False)

    assigned_by = models.ForeignKey('users_app.Profile', models.CASCADE, verbose_name='Кто назначил',
                                    related_name='tasks_assigned')
    assigned_to = models.ForeignKey('users_app.Profile', models.CASCADE, verbose_name='Кому назначено',
                                    related_name='tasks_taken')

    attachment = models.OneToOneField('common_models_app.Attachment', models.CASCADE, verbose_name='Вложение к заданию',
                                      null=True, blank=True)

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'
        ordering = ('id',)

    def __str__(self):
        return f'{self.summary}, для {self.assigned_to.user.last_name} {self.assigned_to.user.first_name}'
