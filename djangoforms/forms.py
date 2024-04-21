from django import forms

class StudentForm(forms.Form):

    CHOICES = (
        ('Male','Male'),
        ('Female','Female'),
        ('Others','Other')
        )
    
    name = forms.CharField(label= 'Name', max_length=20)
    email = forms.EmailField(label= 'Email')
    gender = forms.ChoiceField(label= 'Gender', choices=CHOICES)
    message = forms.CharField(label='Your Message', widget=forms.Textarea)


