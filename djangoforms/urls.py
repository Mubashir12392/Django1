from django.urls import path
from .views import StudentView, student_list, student_detail, StudentUpdate

urlpatterns = [
    path('studentform/', StudentView.as_view()),
    path('students/', student_list, name='students'),
    path('student/<int:id>/',student_detail, name='student_detail'),
    path('student/<int:pk>/update', StudentUpdate.as_view(), name='student_update')
    
]
