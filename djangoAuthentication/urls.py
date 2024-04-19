from django.urls import path
from .views import SignUp, success

urlpatterns = [
    path('signup/', SignUp.as_view()),
    path('signup/success/', success)
]