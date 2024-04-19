from django.db import models

# Create your models here.

class MyModel(models.Model):

    CHOICES = (
        ('M','Male'),
        ('F','Female'),
        ('O','Others')
        )

    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, unique=True)
    gender = models.CharField(max_length=50, choices=CHOICES)
    message = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = ("MyModel")
        verbose_name_plural = ("MyModels")

    def __str__(self):
        return self.name

    