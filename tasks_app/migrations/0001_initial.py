# Generated by Django 2.2.4 on 2019-09-21 16:09

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summary', models.CharField(max_length=128, verbose_name='Краткое описание')),
                ('description', models.TextField(verbose_name='Описание')),
                ('date_of_issue', models.DateField(auto_now_add=True, verbose_name='Дата назначения')),
                ('done', models.BooleanField(default=False, verbose_name='Выполнено')),
                ('dead_line', models.DateField(blank=True, null=True, verbose_name='Срок исполнения')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарий')),
            ],
            options={
                'verbose_name': 'Задание',
                'verbose_name_plural': 'Задания',
            },
        ),
    ]
