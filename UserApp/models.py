from django.db import models
from cloudinary.models import CloudinaryField

class Users(models.Model):
    id = models.AutoField(primary_key=True, db_column="id")
    name = models.CharField(max_length=500, blank=False,  db_column="name")
    email = models.EmailField(max_length=500, unique=True, blank=False,  db_column="email")
    password = models.CharField(max_length=500,  db_column="password")

    def __str__(self):
        return self.ID

class Data(models.Model):
    id = models.AutoField(primary_key=True,  db_column="id")
    user_id = models.ForeignKey(Users, related_name='data' ,on_delete=models.CASCADE, blank=False,  db_column="user_id")
    label = models.CharField(max_length=500, blank=False,  db_column="label")
    sound_uri = models.TextField(blank=False,  db_column="sound_uri")
    date_created = models.DateTimeField(blank=True,  db_column="date_created", auto_now_add = True, auto_now = False)
    
    