from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.ListCreateCourse.as_view(), name='courses'),
    path("<int:pk>/", views.RetrieveUpdateDestroyCourse.as_view(), name="detail"),
    path('<int:pk>/reviews/', views.ListCreateReview.as_view(), name="review_list"),
    path('<int:course_pk>/reviews/<int:pk>/',
         views.RetrieveUpdateDestroyReview.as_view(), name='review_detail'),
]
