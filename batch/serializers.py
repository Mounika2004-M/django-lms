from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Batch
from course.models import Course
from course.serializers import CourseSerializer, TrainerSerializer

User = get_user_model()

class BatchSerializer(serializers.ModelSerializer):
    # Display course details in GET
    course = CourseSerializer(read_only=True)
    # Write-only field to assign course by ID
    course_id = serializers.PrimaryKeyRelatedField(
        queryset=Course.objects.all(), write_only=True, source='course'
    )

    # Learners (IDs for POST, nested info for GET)
    learners = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.filter(role='LEARNER'),
        many=True
    )
    learners_details = serializers.SerializerMethodField(read_only=True)

    # Trainer (ID for POST, nested info for GET)
    trainners = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.filter(role='TRAINER')
    )
    trainners_details = TrainerSerializer(source='trainners', read_only=True)

    class Meta:
        model = Batch
        fields = [
            'id',
            'name',
            'course',
            'course_id',
            'start_date',
            'end_date',
            'learners',
            'learners_details',
            'trainners',
            'trainners_details'
        ]

    def get_learners_details(self, obj):
        # Only include users with role='LEARNER'
        learners = obj.learners.filter(role='LEARNER')
        return [{'id': u.id, 'username': u.username, 'email': u.email} for u in learners]
