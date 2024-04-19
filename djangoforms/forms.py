from django import forms

class MyForm(forms.Form):

    CHOICES = (
        ('M','Male'),
        ('F','Female'),
        ('O','Other')
        )
    
    name = forms.CharField(label= 'Name', max_length=20)
    email = forms.EmailField(label= 'Email')
    gender = forms.CharField(label= 'Gender', widget=forms.Select(choices=CHOICES))
    message = forms.CharField(label='Your Message', widget=forms.Textarea)


