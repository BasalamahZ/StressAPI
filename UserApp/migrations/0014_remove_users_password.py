# Generated by Django 4.2.6 on 2023-11-03 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0013_delete_soundupload'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='password',
        ),
    ]