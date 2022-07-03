from turtle import update
from rest_framework import serializers
from .models import account
from .models import History


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = account
        fields = ['pk','user','phone', 'balance',]
class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ['pk','history']

