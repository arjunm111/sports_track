from django.contrib import admin
from .models import Department, Programme, Student, Item, Teacher, Tutor

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('dept_id', 'dept_name')
    search_fields = ('dept_name',)

@admin.register(Programme)
class ProgrammeAdmin(admin.ModelAdmin):
    list_display = ('pgm_id', 'pgm_name', 'dept')
    list_filter = ('dept',)
    search_fields = ('pgm_name',)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('stud_id', 'name', 'reg_num', 'pgm', 'year_adm', 'gender', 'email', 'phone', 'dob')
    list_filter = ('pgm', 'year_adm', 'gender')
    search_fields = ('name', 'reg_num', 'email')
    ordering = ('-year_adm',)

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('item_id', 'item_name', 'type', 'gender')
    search_fields = ('item_name',)
    list_filter = ('type', 'gender')


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('teacher_id', 'teacher_name', 'dept_id', 'phone_no', 'role')
    search_fields = ('teacher_name', 'phone_no', 'role')
    list_filter = ('dept_id', 'role')
    ordering = ('teacher_id',)

@admin.register(Tutor)
class TutorAdmin(admin.ModelAdmin):
    list_display = ('tutor_id', 'teacher', 'programme', 'year_adm')
    search_fields = ('teacher__teacher_name', 'programme__pgm_name')
    list_filter = ('year_adm', 'programme')
    ordering = ('tutor_id',)