from django.urls import path
from .views import CustomSignUpView, CustomSigninView

urlpatterns = [
    path('signup/', CustomSignUpView.as_view()),
    path('signin/', CustomSigninView.as_view(), name='signin')
    
]