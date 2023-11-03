from rest_framework import serializers
from UserApp.models import Users,Data

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model=Data
        fields=('id', 'user_id', 'label', 'sound_uri', 'date_created')

class UsersSerializer(serializers.ModelSerializer):
    data = DataSerializer(many=True, read_only=True)

    class Meta:
        model=Users
        fields=('id', 'name', 'email', 'password', 'data')
