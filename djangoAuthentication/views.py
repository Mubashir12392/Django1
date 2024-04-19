from django.shortcuts import render
from django.views.generic import FormView
from .forms import CustomUserForm
from django.contrib.auth.models import User

# Create your views here.
class SignUp(FormView):
    template_name = 'signup.html'
    form_class = CustomUserForm
    success_url = 'success/'

    def form_valid(self, form):

        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        email = form.cleaned_data['email']
        username = form.cleaned_data['username']
        password = form.cleaned_data['password1']

        User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)

        return super().form_valid(form)
    
def success(request):
    return render(request, 'success.html')