from django.urls import path
from .views import MyView, Mysuccess

urlpatterns = [
    path('myform/', MyView.as_view()),
    path('myform/mysuccess/', Mysuccess)
]
