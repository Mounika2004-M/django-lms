from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Course  # import your Course model

User = get_user_model()  # get the actual user model

class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class CourseSerializer(serializers.ModelSerializer):
    # trainers field for assigning trainers (ManyToMany or PrimaryKeyRelated)
    trainers = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.filter(role='TRAINER'), 
        many=True
    )
    # nested serializer to display trainer details
    trainers_details = TrainerSerializer(source='trainers', many=True, read_only=True)

    class Meta:
        model = Course  # ✅ use Course model here, not User
        fields = ['id','title', 'desc', 'dur_weeks', 'trainers', 'trainers_details', 'created_at']

        





