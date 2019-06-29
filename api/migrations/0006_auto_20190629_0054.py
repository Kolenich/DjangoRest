# Generated by Django 2.2.2 on 2019-06-28 21:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('api', '0005_auto_20190629_0010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='avatar',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.Avatar',
                                       verbose_name='Аватар'),
        ),
    ]
