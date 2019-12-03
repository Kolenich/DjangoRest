# Generated by Django 2.2.7 on 2019-12-03 19:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('common_models_app', '0001_initial'),
        ('tasks_app', '0004_auto_20190926_0016'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='attachment',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='task',
                                       to='common_models_app.Attachment', verbose_name='Вложение к заданию'),
        ),
    ]