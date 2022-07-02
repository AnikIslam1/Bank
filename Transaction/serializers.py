from turtle import update
from rest_framework import serializers
from .models import account


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = account
        fields = ['pk','user','phone', 'balance','history']

