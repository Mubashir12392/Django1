from django.contrib.auth.models import User
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic import CreateView,FormView

from .forms import CustomSignUpForm, CustomSignInForm


# Create your views here.

# ----- Custom User Signup View ------

class CustomSignUpView(CreateView):
    model = User
    template_name = 'signup.html'
    form_class = CustomSignUpForm
    success_url = reverse_lazy('signin')


# --- Custom User Login  View -----

class CustomSigninView(FormView):
    form_class = CustomSignInForm
    template_name = 'signin.html'
    success_url = reverse_lazy('students')

    # Make the user login
    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return super().form_valid(form)
