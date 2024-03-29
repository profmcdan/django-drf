# from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework import status


from . import models
from . import serializers
# Create your views here.


class ListCreateCourse(generics.ListCreateAPIView):
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer


class RetrieveUpdateDestroyCourse(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer


class ListCreateReview(generics.ListCreateAPIView):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer

    # def get_queryset(self):
    #     return self.queryset.filter(course_id=self.kwargs.get('pk'))

    # def perform_create(self, serializer):
    #     course = get_object_or_404(
    #         self.get_queryset(), pk=self.kwargs.get('pk'))
    #     serializer.save(course=course)


class RetrieveUpdateDestroyReview(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer

    def get_object(self):
        return get_object_or_404(self.get_queryset(),
                                 course_id=self.kwargs.get('course_pk'),
                                 pk=self.kwargs.get('pk'))
