from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from students import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # homepage
    path('student/', include('students.urls')),  # 👈 forward student module
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)