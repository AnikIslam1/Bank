from rest_framework import serializers
from .models import customer



class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = customer
        fields = ['pk','name', 'balance']