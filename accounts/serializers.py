from rest_framework import serializers
from .models import User, Score

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'name', 'last_name', 'description', 'image',]


class TopUserSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    total_score = serializers.IntegerField()
    username = serializers.CharField()
    image = serializers.CharField()
