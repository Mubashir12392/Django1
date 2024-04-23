
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


# --- Custom User Sign Up Form

class CustomSignUpForm(UserCreationForm):
    # We can add here our custom Changes
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
    
    
# ---- Custom User Sign in Form

class CustomSignInForm(AuthenticationForm):
    pass             # We can also Customize it