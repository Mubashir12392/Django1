from django.contrib import admin
from .models import MyModel
# Register your models here.


@admin.register(MyModel)
class StudentData(admin.ModelAdmin):
    list_display = ['name','age']
    # actions_on_bottom = True
    

