from django.db import models
from django.contrib.auth.models import User


class Department(models.Model):
    dept_id = models.AutoField(primary_key=True)
    dept_name = models.CharField(max_length=255)

class Programme(models.Model):
    pgm_id = models.AutoField(primary_key=True)
    pgm_name = models.CharField(max_length=255)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)

class Student(models.Model):
    stud_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    reg_num = models.CharField(max_length=255,unique=True)
    pgm = models.ForeignKey(Programme, on_delete=models.CASCADE)
    year_adm = models.IntegerField()
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)

class Teacher(models.Model):
    teacher_id = models.AutoField(primary_key=True)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    phone_no = models.CharField(max_length=20)
    role = models.CharField(max_length=255)

class Tutor(models.Model):
    tutor_id = models.AutoField(primary_key=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    pgm = models.ForeignKey(Programme, on_delete=models.CASCADE)
    year_adm = models.IntegerField()

class Item(models.Model):
    item_id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)

class StudentItem(models.Model):
    stud = models.ForeignKey(Student, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    year = models.IntegerField()
    class Meta:
        unique_together = ('stud', 'item')

class Hour(models.Model):
    hour_id = models.AutoField(primary_key=True)
    date = models.DateField()
    hour_no = models.IntegerField()
    status = models.CharField(max_length=255)

class PresentDetails(models.Model):
    hour = models.ForeignKey(Hour, on_delete=models.CASCADE)
    stud = models.ForeignKey(Student, on_delete=models.CASCADE)
    class Meta:
        unique_together = ('hour', 'stud')

class Status(models.Model):
    status_id = models.AutoField(primary_key=True)
    status_desc = models.CharField(max_length=255)

class Request(models.Model):
    PENDING = 'pending'
    APPROVED = 'approved'
    REJECTED = 'rejected'

    APPROVAL_STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (APPROVED, 'Approved'),
        (REJECTED, 'Rejected'),
    ]

    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)  # Allow null user
    request_title = models.CharField(max_length=255)
    request_description = models.TextField()
    status = models.CharField(
        max_length=10,
        choices=APPROVAL_STATUS_CHOICES,
        default=PENDING
    )
    created_at = models.DateTimeField(auto_now_add=True)
    approved_by = models.ForeignKey(User, null=True, blank=True, related_name='approved_requests', on_delete=models.SET_NULL)
    approved_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.request_title
