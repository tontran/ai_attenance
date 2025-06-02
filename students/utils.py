import numpy as np
from deepface import DeepFace
from PIL import Image
import os
from scipy.spatial.distance import cosine
from .models import Student, Attendance
from datetime import datetime

def generate_face_embedding(image_path, student_id):
    embedding_obj = DeepFace.represent(img_path=image_path, model_name="Facenet")[0]
    embedding = embedding_obj["embedding"]

    # ✅ Ensure folder exists
    embedding_dir = "media/embeddings"
    os.makedirs(embedding_dir, exist_ok=True)

    save_path = f"{embedding_dir}/{student_id}.npy"
    np.save(save_path, embedding)
    return save_path

def mark_attendance_from_image(class_image_path):
    detected_faces = DeepFace.extract_faces(img_path=class_image_path, enforce_detection=False)
    registered_students = Student.objects.all()

    for face in detected_faces:
        new_embedding = DeepFace.represent(face["face"], model_name="Facenet")[0]["embedding"]

        matched_student = None
        best_score = 1.0
        for student in registered_students:
            if student.embedding_path and os.path.exists(student.embedding_path):
                known_embedding = np.load(student.embedding_path)
                score = cosine(new_embedding, known_embedding)
                if score < 0.5 and score < best_score:
                    matched_student = student
                    best_score = score

        if matched_student:
            Attendance.objects.get_or_create(
                student=matched_student,
                date=datetime.today().date(),
                defaults={"present": True, "confidence": round(1 - best_score, 2)}
            )