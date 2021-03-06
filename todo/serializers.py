from rest_framework import serializers
from .models import Item
from django.contrib.auth.models import User

class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'