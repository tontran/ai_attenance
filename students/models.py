from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    selfie = models.ImageField(upload_to="selfies/")
    embedding_path = models.FilePathField(
        path="media/embeddings",
        match=".*\.npy$", recursive=True, allow_files=True, blank=True, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)  # ✅ Add this line

    def __str__(self):
        return self.name

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    present = models.BooleanField(default=False)
    confidence = models.FloatField(default=0.0)
