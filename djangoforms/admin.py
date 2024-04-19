from django.contrib import admin
from .models import MyModel

# Register your models here.

@admin.register(MyModel)
class MyModelData(admin.ModelAdmin):
    pass