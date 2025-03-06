from django.db import models
from django.contrib.auth.models import User

# Ensure Teacher and Programme models are defined first
class Department(models.Model):
    dept_id = models.AutoField(primary_key=True)
    dept_name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.dept_name

class Programme(models.Model):
    pgm_id = models.AutoField(primary_key=True)
    pgm_name = models.CharField(max_length=255)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.pgm_name

class Student(models.Model):
    stud_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    reg_num = models.CharField(max_length=255, unique=True)
    pgm = models.ForeignKey(Programme, on_delete=models.CASCADE)
    year_adm = models.IntegerField()
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    dob = models.DateField()
    photo = models.ImageField(upload_to='sports_attendance/student_photos/', null=True, blank=True)
    
    def __str__(self):
        return self.name
class Teacher(models.Model):
    teacher_id = models.AutoField(primary_key=True)
    teacher_name = models.CharField(max_length=255, default="")  # Ensure a default value
    dept_id = models.IntegerField()
    phone_no = models.CharField(max_length=15)
    role = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.teacher_id} - {self.teacher_name} - {self.role}"



# Now we define the Tutor model after Teacher is defined
class Tutor(models.Model):
    tutor_id = models.AutoField(primary_key=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)  # Correct reference
    programme = models.ForeignKey(Programme, on_delete=models.CASCADE)
    year_adm = models.IntegerField()

    def __str__(self):
        return f"Tutor ID: {self.tutor_id}, Teacher: {self.teacher.teacher_name}, Programme: {self.programme.pgm_name}"


class Item(models.Model):
    item_id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=255)
    TYPE_CHOICES = [
        ('Individual', 'Individual'),
        ('Group', 'Group'),
    ]
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
