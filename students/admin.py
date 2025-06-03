from django.contrib import admin
from django.utils.html import format_html
from .models import Student, Attendance

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'created_at', 'selfie_preview')
    search_fields = ('name', 'email', 'phone')
    readonly_fields = ['selfie_preview', 'embedding_path']
    list_filter = ['created_at']
    ordering = ['-created_at']  # newest first

    def selfie_preview(self, obj):
        if obj.selfie:
            return format_html('<img src="{}" width="120" style="border-radius:8px;" />', obj.selfie.url)
        return "No Image"
    
    selfie_preview.short_description = "📷 Selfie"

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'date', 'present', 'confidence')
    list_filter = ('date', 'present')
    search_fields = ('student__name',)
