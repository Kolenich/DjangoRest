from django.db import models


# Create your models here.

class Employee(models.Model):
    first_name = models.CharField(max_length=64, verbose_name='Имя')
    last_name = models.CharField(max_length=64, verbose_name='Фамилия')
    middle_name = models.CharField(max_length=64, null=True, blank=True, verbose_name='Отчество')
    phone = models.CharField(max_length=32, null=True, blank=True, verbose_name='Телефон')
    email = models.EmailField(unique=True, verbose_name='Электронная почта')
    age = models.PositiveSmallIntegerField(verbose_name='Возраст')
    date_of_birth = models.DateField(verbose_name='Дата рождения')
    registration_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')
    organization = models.ForeignKey('Organization', on_delete=models.CASCADE, null=True, blank=True,
                                     related_name='employees', verbose_name='Организация')

    class Meta:
        verbose_name = 'Покупатель'
        verbose_name_plural = 'Покупатели'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Organization(models.Model):
    full_name = models.CharField(max_length=128, verbose_name='Полное название организации')
    short_name = models.CharField(max_length=128, verbose_name='Сокращенное название организации')
    registration_date = models.DateField(auto_now_add=True, verbose_name='Дата регистрации')
    inn = models.CharField(max_length=16, verbose_name='ИНН')
    kpp = models.CharField(max_length=16, verbose_name='КПП')
    ogrn = models.CharField(max_length=32, verbose_name='ОГРН')
    okved_code = models.CharField(max_length=32, verbose_name='Код ОКВЭД')
    okved_name = models.CharField(max_length=512, verbose_name='Расшифровка ОКВЭД')

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'
        unique_together = ('inn', 'kpp')

    def __str__(self):
        return f'{self.full_name}'
