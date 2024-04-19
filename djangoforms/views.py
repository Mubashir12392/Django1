from django.shortcuts import render
from django.views.generic import FormView
from .forms import MyForm
from .models import MyModel

# Create your views here.


class MyView(FormView):
    template_name = 'myform.html'
    form_class = MyForm
    success_url = 'success/'

    def form_valid(self, form):

        # save the form data in variable
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        gender = form.cleaned_data['gender']
        message = form.cleaned_data['message']

        # Create and save the new instance of the model
        MyModel.objects.create(name=name, email=email, gender=gender, message=message)

        return super().form_valid(form)
    

def success(request):
    return render(request, 'success.html')
