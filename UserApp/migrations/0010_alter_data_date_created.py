# Generated by Django 4.2.6 on 2023-10-31 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0009_alter_data_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, db_column='date_created'),
        ),
    ]