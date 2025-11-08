from rest_framework import serializers
from .models import User
from django.contrib.auth import get_user_model

user = get_user_model()

class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ['id', 'username', 'email']
       

class CourseSerializer(serializers.ModelSerializer):
    trainers= serializers.PrimaryKeyRelatedField(queryset=user.objects.filter(role='TRAINER'), many=True)
    trainers_details = TrainerSerializer(source='trainers', many=True, read_only=True)
    class Meta:
        model = user
        fields = ['id', 'title', 'desc', 'dur_weeks', 'trainers', 'trainers_details', 'created_at']