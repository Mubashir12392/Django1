from django.db import models

# Create your models here.
class Student(models.Model):
    GENDERS = (
        ('M','Male'),
        ('F','Female'),
        ('O','Others'))


    student_name = models.CharField(max_length=50)
    age = models.PositiveSmallIntegerField(null=True)
    gender = models.CharField(max_length=50, choices=GENDERS)
    height = models.IntegerField(blank=True, null=True)
    grade = models.ForeignKey('Grade', on_delete=models.CASCADE, null=True)
    teachers = models.ManyToManyField("Teacher")
    subjects = models.ManyToManyField("Subject")
    school = models.ForeignKey("School", on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return self.student_name

class Teacher(models.Model):
    GENDERS = (
        ('M','Male'),
        ('F','Female'),
        ('O','Others'))
    
    teacher_name = models.CharField(max_length=50)
    age = models.PositiveSmallIntegerField(null=True, default=18)
    gender = models.CharField(max_length=50, choices=GENDERS)
    height = models.PositiveSmallIntegerField(blank=True, null=True)
    incharge_grade = models.OneToOneField("Grade", on_delete=models.CASCADE, null=True)
    specialized_subject = models.ForeignKey("Subject", on_delete=models.CASCADE, null=True)
    school = models.ForeignKey("School", on_delete=models.CASCADE, null=True)
    def __str__(self) -> str:
        return self.teacher_name

class Grade(models.Model):
    grade_name = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.grade_name

class Subject(models.Model):
    subject_name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.subject_name

class School(models.Model):
    school_name = models.CharField(max_length=50)
    founder = models.CharField(max_length=50, null=True)
    established_data = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)

    def __str__(self) -> str:
        return self.school_name

