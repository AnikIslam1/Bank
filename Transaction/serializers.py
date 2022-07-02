from turtle import update
from rest_framework import serializers
from .models import account


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = account
        fields = ['pk','user', 'balance','history']

