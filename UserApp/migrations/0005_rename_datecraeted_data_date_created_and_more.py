# Generated by Django 4.2.6 on 2023-10-31 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0004_data'),
    ]

    operations = [
        migrations.RenameField(
            model_name='data',
            old_name='DateCraeted',
            new_name='date_created',
        ),
        migrations.RenameField(
            model_name='data',
            old_name='ID',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='data',
            old_name='Label',
            new_name='label',
        ),
        migrations.RenameField(
            model_name='data',
            old_name='UserID',
            new_name='user_id',
        ),
        migrations.RenameField(
            model_name='users',
            old_name='Email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='users',
            old_name='ID',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='users',
            old_name='Name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='users',
            old_name='Password',
            new_name='password',
        ),
    ]
