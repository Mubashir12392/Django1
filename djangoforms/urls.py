from django.urls import path
from .views import StudentAdd, Studentlist, StudentDetail, StudentUpdate, StudentDelete

urlpatterns = [
    path('studentform/', StudentAdd.as_view(), name='student_add'),
    path('students/', Studentlist.as_view(), name='students'),
    path('student/<int:pk>/',StudentDetail.as_view(), name='student_detail'),
    path('student/<int:pk>/update/', StudentUpdate.as_view(), name='student_update'),
    path('student/<int:pk>/delete/',StudentDelete.as_view(), name='student_delete')
    
]
