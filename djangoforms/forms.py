from django import forms
from .models import Student

class StudentForm(forms.ModelForm):

    CHOICES = (
        ('Male','Male'),
        ('Female','Female'),
        ('Others','Other')
        )
    
    name = forms.CharField(label= 'Name', max_length=20)
    email = forms.EmailField(label= 'Email')
    gender = forms.ChoiceField(label= 'Gender', choices=CHOICES)
    message = forms.CharField(label='Your Message', widget=forms.Textarea)

    class Meta:
        model = Student
        fields = ['name', 'email', 'gender', 'message']



