from django.db import models

# Create your models here.

class MyModel(models.Model):
    CHOICES = (
        ('M','Male'),
        ('F','Female')
               )

    name = models.CharField(max_length=50, null=True)
    age = models.PositiveSmallIntegerField(null=True)
    gender = models.CharField(max_length=50, choices=CHOICES, null=True)
    city = models.CharField(max_length=50, null=True)

    def __str__(self) -> str:
        return f'{self.name}' 


   