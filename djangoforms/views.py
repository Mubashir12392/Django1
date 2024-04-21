from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView, UpdateView, DeleteView
from .forms import StudentForm
from .models import Student

# Create your views here.

# CRUD ----- CREATE
class StudentView(FormView):
    template_name = 'studentform.html'
    form_class = StudentForm
    success_url = reverse_lazy ('students')

    def form_valid(self, form):

        # save the form data in variable
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        gender = form.cleaned_data['gender']
        message = form.cleaned_data['message']

        # Create and save the new instance of the model
        Student.objects.create(name=name, email=email, gender=gender, message=message)

        return super().form_valid(form)
    

# CRUD ------ READ
def student_list(request):
    students = Student.objects.all()
    context = {
        'students' : students
    }
    return render(request, 'studentlist.html', context=context)

def student_detail(request, id):
    student = Student.objects.get(id=id)
    context = {
        'student' : student
    }
    return render(request, 'studentdetail.html', context=context)


# CRUD ----- UPDATE

class StudentUpdate(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'studentform.html'
    success_url = reverse_lazy('students')

    def get_object(self, queryset=None):
        # Get the student object to update
        return self.model.objects.get(id=self.kwargs['pk'])

