from django.urls import path
from .views import MyView, success

urlpatterns = [
    path('myform/', MyView.as_view()),
    path('myform/success/', success)
]
