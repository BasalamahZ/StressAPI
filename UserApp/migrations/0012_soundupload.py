# Generated by Django 4.2.6 on 2023-11-03 09:13

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0011_data_sound_uri'),
    ]

    operations = [
        migrations.CreateModel(
            name='SoundUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sound', cloudinary.models.CloudinaryField(max_length=255, verbose_name='sound')),
                ('created_at', models.DateTimeField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'İmages',
            },
        ),
    ]
