from django import forms
from .models import Department,Programme,Teacher,Tutor,Item,StudentItem,Hour,PresentDetails,Status

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
        

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['dept', 'phone_no', 'role']  # These are the fields you want in the form
        

class TutorForm(forms.ModelForm):
    class Meta:
        model = Tutor
        fields = ['teacher', 'pgm', 'year_adm']  # Fields for the form
        


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['item_name', 'type', 'gender']  # These are the fields we want in the form
        


class StudentItemForm(forms.ModelForm):
    class Meta:
        model = StudentItem
        fields = ['stud', 'item', 'year']  # These are the fields we want in the form
        

class HourForm(forms.ModelForm):
    class Meta:
        model = Hour
        fields = ['date', 'hour_no', 'status']  # Fields we want in the form


class PresentDetailsForm(forms.ModelForm):
    class Meta:
        model = PresentDetails
        fields = ['hour', 'stud']  # Fields we want in the form
        


class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['status_desc']  # Only status_desc field is needed for the form






