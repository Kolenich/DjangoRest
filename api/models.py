from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver


# Create your models here.

class Employee(models.Model):
    SEX = [('male', 'Мужской'), ('female', 'Женский')]

    first_name = models.CharField(verbose_name='Имя', max_length=64)
    last_name = models.CharField(verbose_name='Фамилия', max_length=64)
    middle_name = models.CharField(verbose_name='Отчество', max_length=64, null=True, blank=True)
    phone = models.CharField(verbose_name='Телефон', max_length=32, null=True, blank=True)
    email = models.EmailField(verbose_name='Электронная почта', unique=True)
    age = models.PositiveSmallIntegerField(verbose_name='Возраст')
    date_of_birth = models.DateField(verbose_name='Дата рождения')
    sex = models.CharField(verbose_name='Пол', max_length=6, choices=SEX, default='male')
    registration_date = models.DateTimeField(verbose_name='Дата регистрации', auto_now_add=True)
    attachment = models.ForeignKey('Attachment', verbose_name='Фотография', on_delete=models.CASCADE, null=True,
                                   blank=True)
    organization = models.ForeignKey('Organization', verbose_name='Организация', on_delete=models.CASCADE, null=True,
                                     blank=True, related_name='employees')

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
        ordering = ('id',)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Organization(models.Model):
    full_name = models.CharField(verbose_name='Полное название организации', max_length=128)
    short_name = models.CharField(verbose_name='Сокращенное название организации', max_length=128)
    registration_date = models.DateField(verbose_name='Дата регистрации', auto_now_add=True)
    inn = models.CharField(verbose_name='ИНН', max_length=16)
    kpp = models.CharField(verbose_name='КПП', max_length=16)
    ogrn = models.CharField(verbose_name='ОГРН', max_length=32)
    okved_code = models.CharField(verbose_name='Код ОКВЭД', max_length=32)
    okved_name = models.CharField(verbose_name='Расшифровка ОКВЭД', max_length=512)

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'
        unique_together = ('inn', 'kpp')
        ordering = ('id',)

    def __str__(self):
        return f'{self.full_name}'


class Attachment(models.Model):
    file = models.ImageField(verbose_name='Файл', upload_to='attachments')
    file_name = models.CharField(verbose_name='Имя файла', max_length=500)
    file_mime = models.CharField(verbose_name='Расширение файла', max_length=500)
    file_size = models.IntegerField(verbose_name='Размер файла')
    uploaded = models.DateTimeField(verbose_name="Время создания", auto_now_add=True)

    class Meta:
        verbose_name = 'Вложение'
        verbose_name_plural = 'Вложения'
        ordering = ('id',)

    def __str__(self):
        return self.file_name


@receiver(post_delete, sender=Attachment)
def submission_delete(instance: Attachment, **kwargs):
    """
    Функция, которая вызывается после удаления объекта модели Attachment
    :param instance: объект модели Attachment
    :param kwargs: дополнительные параметры
    :return: удаляет файл с сервера
    """
    instance.file.delete(False)