from django.urls import path
from .views import (
    StudentListView, StudentDetailView, StudentCreateView, 
    StudentUpdateView, StudentDeleteView
)

urlpatterns = [
    path('', StudentListView.as_view(), name='student_list'),
    path('<int:pk>/', StudentDetailView.as_view(), name='student_detail'),
    path('add/', StudentCreateView.as_view(), name='add_student'),
    path('<int:pk>/edit/', StudentUpdateView.as_view(), name='edit_student'),
    path('<int:pk>/delete/', StudentDeleteView.as_view(), name='delete_student'),
]
