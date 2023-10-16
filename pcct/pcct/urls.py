from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from students_monitoring import views

router = routers.DefaultRouter()
router.register(r'student', views.StudentView, 'student')

urlpatterns = [
    path("", include(router.urls)),
]