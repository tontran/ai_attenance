from django.shortcuts import render, redirect
from django.utils.timezone import now
import base64
from django.core.files.base import ContentFile
from .models import Student, Attendance
from .forms import StudentForm
from .utils import generate_face_embedding

def home(request):
    return redirect('register_student')

def register_student(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        selfie_data = request.POST.get('selfie_data')

        format, imgstr = selfie_data.split(';base64,')
        ext = format.split('/')[-1]
        selfie_file = ContentFile(base64.b64decode(imgstr), name=f"{name.replace(' ', '_')}.{ext}")

        student = Student.objects.create(
            name=name,
            email=email,
            phone=phone,
            selfie=selfie_file
        )
        embedding_path = generate_face_embedding(student.selfie.path, student.id)
        student.embedding_path = embedding_path
        student.save()

        return redirect('register_success')

    return render(request, 'students/register.html')

def attendance_dashboard(request):
    today = now().date()
    records = Attendance.objects.filter(date=today).select_related('student')
    return render(request, 'students/dashboard.html', {'records': records, 'today': today})


def register_success(request):
    return render(request, 'students/register_success.html')