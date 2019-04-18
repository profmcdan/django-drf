from rest_framework import serializers
from . import models


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Review
        extra_kwargs = {
            "email": {"write_only": True}
        }
        fields = (
            'id', 'course', 'name', 'email', 'comment', 'rating', 'created_at'
        )


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = (
            'id', 'title', 'url'
        )
