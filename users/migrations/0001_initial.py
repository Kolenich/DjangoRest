# Generated by Django 3.1.2 on 2020-10-20 15:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('common_models', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('middle_name', models.CharField(blank=True, max_length=128, null=True, verbose_name='Отчество')),
                ('phone', models.CharField(blank=True, max_length=32, null=True, verbose_name='Телефон')),
                ('mailing', models.BooleanField(blank=True, default=False, verbose_name='Рассылка на почту')),
                ('avatar', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                                to='common_models.attachment', verbose_name='Аватар')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL,
                                              verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Профиль пользователя',
                'verbose_name_plural': 'Профили пользователей',
                'db_table': 'profiles',
            },
        ),
    ]
