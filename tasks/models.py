"""Модели приложения TasksApp."""

from django.contrib.admin import site
from django.db import models
from django.template.loader import render_to_string


# Create your models here.

@site.register
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

    def to_websocket(self):
        from websockets.publisher import Publisher
        from tasks.serializers import TaskDashboardSerializer

        Publisher(f'tasks_{self.assigned_to.username}').publish(message=TaskDashboardSerializer(self).data)

    @property
    def email_template(self):
        """
        Метод получения шаблона для отправки уведомления на почту.

        :return: строка шаблона
        """
        context = {
            'summary': self.summary,
            'description': self.description,
            'comment': self.comment,
            'date_of_issue': self.date_of_issue,
            'dead_line': self.dead_line,
        }
        return render_to_string('email_notification.html', context)

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'
        db_table = 'tasks'

    def __str__(self):
        return f'{self.summary}, для {self.assigned_to.last_name} {self.assigned_to.first_name}'
