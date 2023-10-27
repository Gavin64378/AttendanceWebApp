"""Defines URL patterns for attendance_tracker"""

from django.urls import path
from . import views

app_name = 'attendance_tracker'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
      # Login page
      path('login/', views.login, name='login'),
]