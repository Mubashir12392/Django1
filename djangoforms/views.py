from django.db.models.base import Model as Model
from django.urls import reverse_lazy
from django.views.generic import CreateView,ListView,DetailView,UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import StudentForm
from .models import Student

# Django CRUD, USING FORMS AND CLASS BASED GENERIC VIEWS
# Create your views here.

# CRUD ----- CREATE
class StudentAdd(LoginRequiredMixin, CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'studentform.html'
    success_url = reverse_lazy('students')

# CRUD ------ READ
class Studentlist(LoginRequiredMixin, ListView):
    model = Student
    template_name = 'studentlist.html'
    context_object_name = 'students'


class StudentDetail(LoginRequiredMixin, DetailView):
    model = Student
    template_name = 'studentdetail.html'
    context_object_name = 'student'


# CRUD ----- UPDATE
class StudentUpdate(LoginRequiredMixin, UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'editstudent.html'
    context_object_name = 'student'
    success_url = reverse_lazy('students')


# CRUD ----- DELETE
class StudentDelete(LoginRequiredMixin, DeleteView):         # Delete button in template must send post request to delete 
    model = Student
    template_name = 'studentdetail.html'
    success_url = reverse_lazy('students')