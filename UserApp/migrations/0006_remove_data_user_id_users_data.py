# Generated by Django 4.2.6 on 2023-10-31 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0005_rename_datecraeted_data_date_created_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data',
            name='user_id',
        ),
        migrations.AddField(
            model_name='users',
            name='data',
            field=models.ManyToManyField(to='UserApp.data'),
        ),
    ]