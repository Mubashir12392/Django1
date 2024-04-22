from django.db import models

# Create your models here.

class Student(models.Model):

    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, unique=True)
    gender = models.CharField(max_length=50)
    message = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = ("Student")
        verbose_name_plural = ("Students")

    def __str__(self):
        return self.name

    