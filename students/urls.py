from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_student, name='register_student'),
    path('register/success/', views.register_success, name='register_success'),
    path('dashboard/', views.attendance_dashboard, name='attendance_dashboard'),
]
