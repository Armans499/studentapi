from django.urls import path
from . import views

urlpatterns = [
    path('students/',views.student_list,name='student_list'),
    path('students/<int:pk>/',views.student_detail,name='student-detail'),
    path('students/<int:pk>/delete/',views.student_delete,name='stdent-delete'),
]