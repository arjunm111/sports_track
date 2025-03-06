from django import forms
from .models import Department, Programme, Student, Item,Teacher,Tutor

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['dept_name']

class ProgrammeForm(forms.ModelForm):
    class Meta:
        model = Programme
        fields = ['pgm_name', 'dept']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'reg_num', 'pgm', 'year_adm', 'gender', 'email', 'phone', 'dob','photo',]
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
        }

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['item_name', 'type', 'gender']


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['dept_id', 'phone_no', 'role','teacher_name']

class TutorForm(forms.ModelForm):
    class Meta:
        model = Tutor
        fields = ['teacher', 'programme', 'year_adm']
    
    teacher = forms.ModelChoiceField(queryset=Teacher.objects.all(), label="Teacher")
    programme = forms.ModelChoiceField(queryset=Programme.objects.all(), label="Programme")
    year_adm = forms.IntegerField(label="Year of Admission")