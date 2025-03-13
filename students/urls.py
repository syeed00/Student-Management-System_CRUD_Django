from django.urls import path
from .views import student_list, add_student, edit_student, delete_student

urlpatterns = [
    path('', student_list, name='student_list'),
    path('add/', add_student, name='add_student'),
    path('edit/<int:pk>/', edit_student, name='edit_student'),
    path('delete/<int:pk>/', delete_student, name='delete_student'),
]
