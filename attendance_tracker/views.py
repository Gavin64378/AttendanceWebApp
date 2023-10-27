from django.shortcuts import render

# Create your views here.

def index(request):
    """The home page for attendance_tracker."""
    return render(request, 'attendance_tracker/index.html')

def login(request):
    """The login page for attendance_tracker."""
    return render(request, 'attendance_tracker/login.html')
