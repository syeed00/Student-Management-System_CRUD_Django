from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'course')  # Show these fields in the admin panel
    search_fields = ('name', 'email', 'course')  # Enable search
