from django.contrib import admin
from django.urls import path
from students import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('register/', views.register_student, name='register_student'),
    path('dashboard/', views.attendance_dashboard, name='attendance_dashboard'),
    path('register/success/', views.register_success, name='register_success'),
]
