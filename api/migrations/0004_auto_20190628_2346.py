# Generated by Django 2.2.2 on 2019-06-28 20:46

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('api', '0003_auto_20190628_2326'),
    ]

    operations = [
        migrations.RenameField(
            model_name='avatar',
            old_name='file_mime',
            new_name='content_type',
        ),
        migrations.RenameField(
            model_name='avatar',
            old_name='file_size',
            new_name='size',
        ),
    ]