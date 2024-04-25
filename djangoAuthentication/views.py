from django.contrib.auth.models import User
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic import CreateView,FormView

from .forms import CustomSignUpForm, CustomSignInForm
from .backends import CustomAuthBackend


# Create your views here.

# ----- Custom User Signup View ------

class CustomSignUpView(CreateView):
    model = User
    template_name = 'signup.html'
    form_class = CustomSignUpForm
    success_url = reverse_lazy('signin')


# --- Custom User Login  View -----

class CustomSignInView(FormView):
    form_class = CustomSignInForm
    template_name = 'signin.html'
    success_url = reverse_lazy('students')

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        
        custom_backend = CustomAuthBackend()
        user = custom_backend.authenticate(request=self.request, username=username, password=password)

        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        else:
            
            return self.form_invalid(form)