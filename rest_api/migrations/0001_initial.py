# Generated by Django 2.2.4 on 2019-09-21 16:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Avatar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.ImageField(upload_to='avatars', verbose_name='Файл')),
                ('content_type', models.CharField(max_length=16, verbose_name='Тип файла')),
                ('size', models.PositiveIntegerField(verbose_name='Размер файла')),
                ('file_name', models.CharField(max_length=1024, verbose_name='Имя файла')),
            ],
            options={
                'verbose_name': 'Аватар',
                'verbose_name_plural': 'Аватары',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=64, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=64, verbose_name='Фамилия')),
                ('middle_name', models.CharField(blank=True, max_length=64, null=True, verbose_name='Отчество')),
                ('phone', models.CharField(blank=True, max_length=32, null=True, verbose_name='Телефон')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Электронная почта')),
                ('age', models.PositiveSmallIntegerField(verbose_name='Возраст')),
                ('date_of_birth', models.DateField(verbose_name='Дата рождения')),
                ('sex',
                 models.CharField(choices=[('male', 'Мужской'), ('female', 'Женский')], default='male', max_length=6,
                                  verbose_name='Пол')),
                ('registration_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')),
                ('avatar',
                 models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='rest_api.Avatar',
                                      verbose_name='Аватар')),
            ],
            options={
                'verbose_name': 'Сотрудник',
                'verbose_name_plural': 'Сотрудники',
                'ordering': ('id',),
            },
        ),
    ]
