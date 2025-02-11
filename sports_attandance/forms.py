from django import forms
from .models import Department,Programme

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['dept_name']
        widgets = {
            'dept_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Department Name'}),
        }
class ProgrammeForm(forms.ModelForm):
    class Meta:
        model = Programme
        fields = ['pgm_name', 'dept']  # Fields you want to include in the form