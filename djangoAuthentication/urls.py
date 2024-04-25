from django.urls import path
from .views import CustomSignUpView, CustomSignInView

urlpatterns = [
    path('signup/', CustomSignUpView.as_view()),
    path('signin/', CustomSignInView.as_view(), name='signin')
    
]