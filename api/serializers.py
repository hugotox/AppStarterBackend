from django.contrib.auth.models import User, Group
from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'groups']

    groups = PrimaryKeyRelatedField(many=True, read_only=True)


class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name']
