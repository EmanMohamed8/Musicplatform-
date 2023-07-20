from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.db.models import fields

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'bio']
        read_only_fields = ['id']
