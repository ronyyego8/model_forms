from django import forms
from .models import Students

class StudentsForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = ['FirstName', 'LastName', 'emailaddress', 'date_of_birth', 'age']

    widgets = {
        'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
    }
