from django.contrib import admin
from .models import Student
# Register your models here.


@admin.register(Student)
class StudentData(admin.ModelAdmin):
    list_display = ['name','age']
    # actions_on_bottom = True
    

