# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Department,Programme,Teacher,Tutor,Item,StudentItem,Hour,PresentDetails,Status,Student
from .forms import DepartmentForm,ProgrammeForm,TeacherForm,TutorForm,ItemForm,StudentItemForm,HourForm,PresentDetailsForm,StatusForm,StudentForm
from django.http import HttpResponse
def hour_list(request):
    hours = Hour.objects.all()
    return render(request, 'sports_attandance/hour_list.html', {'hours': hours})

# Create a new hour entry (attendance record)
def hour_create(request):
    if request.method == 'POST':
        form = HourForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hour_list')  # Redirect to the list after saving
    else:
        form = HourForm()
    return render(request, 'sports_attandance/hour_form.html', {'form': form})

# Edit an existing hour entry (attendance record)
def hour_edit(request, hour_id):
    hour = get_object_or_404(Hour, id=hour_id)
    if request.method == 'POST':
        form = HourForm(request.POST, instance=hour)
        if form.is_valid():
            form.save()
            return redirect('hour_list')
    else:
        form = HourForm(instance=hour)
    return render(request, 'sports_attandance/hour_form.html', {'form': form})

# Delete an hour entry (attendance record)
def hour_delete(request, hour_id):
    hour = get_object_or_404(Hour, id=hour_id)
    hour.delete()
    return redirect('hour_list')

# View to display the list of departments
def department_list(request):
    departments = Department.objects.all()  # Fetch all departments
    return render(request, 'department_list.html', {'departments': departments})

# View to create a new department
def department_create(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('department_list')  # Redirect to the department list page after creation
    else:
        form = DepartmentForm()
    return render(request, 'department_form.html', {'form': form})

# View to edit an existing department
def department_edit(request, dept_id):
    department = get_object_or_404(Department, dept_id=dept_id)
    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            return redirect('department_list')  # Redirect toTeacher the department list after editing
    else:
        form = DepartmentForm(instance=department)
    return render(request, 'department_form.html', {'form': form})

# View to delete a department
def department_delete(request, dept_id):
    department = get_object_or_404(Department, dept_id=dept_id)
    if request.method == 'POST':
        department.delete()
        return redirect('department_list')  # Redirect to the department list after deletion
    return render(request, 'department_confirm_delete.html', {'department': department})

def home_view(request):
    return render(request, 'home.html')

def programme_list(request):
    programmes = Programme.objects.all()
    return render(request, 'sports_attandance/programme_list.html', {'programmes': programmes})

# Create a new programme
def programme_create(request):
    if request.method == 'POST':
        form = ProgrammeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('programme_list')  # Redirect to the list view after saving
    else:
        form = ProgrammeForm()
    return render(request, 'sports_attandance/programme_form.html', {'form': form})

# Edit an existing programme
def programme_edit(request, pgm_id):
    programme = Programme.objects.get(pgm_id=pgm_id)
    if request.method == 'POST':
        form = ProgrammeForm(request.POST, instance=programme)
        if form.is_valid():
            form.save()
            return redirect('programme_list')
    else:
        form = ProgrammeForm(instance=programme)
    return render(request, 'sports_attandance/programme_form.html', {'form': form})

# Delete an existing programme
def programme_delete(request, pgm_id):
    programme = Programme.objects.get(pgm_id=pgm_id)
    programme.delete()
    return redirect('programme_list')

def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'sports_attandance/teacher_list.html', {'teachers': teachers})

# Create a new teacher
def teacher_create(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teacher_list')  # Redirect to the list view after saving
    else:
        form = TeacherForm()
    return render(request, 'sports_attandance/teacher_form.html', {'form': form})

# Edit an existing teacher
def teacher_edit(request, teacher_id):
    teacher = get_object_or_404(Teacher, teacher_id=teacher_id)
    if request.method == 'POST':
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():from django.shortcuts import render, get_object_or_404, redirect

def teacher_delete(request, teacher_id):
    teacher = get_object_or_404(Teacher, teacher_id=teacher_id)
    teacher.delete()
    return redirect('teacher_list')

def tutor_list(request):
    tutors = Tutor.objects.all()
    return render(request, 'sports_attandance/tutor_list.html', {'tutors': tutors})

# Create a new tutor
def tutor_create(request):
    if request.method == 'POST':
        form = TutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tutor_list')  # Redirect to the tutor list page after saving
    else:
        form = TutorForm()
    return render(request, 'sports_attandance/tutor_form.html', {'form': form})

# Edit an existing tutor
def tutor_edit(request, tutor_id):
    tutor = get_object_or_404(Tutor, tutor_id=tutor_id)
    if request.method == 'POST':
        form = TutorForm(request.POST, instance=tutor)
        if form.is_valid():
            form.save()
            return redirect('tutor_list')
    else:
        form = TutorForm(instance=tutor)
    return render(request, 'sports_attandance/tutor_form.html', {'form': form})

# Delete an existing tutor
def tutor_delete(request, tutor_id):
    tutor = get_object_or_404(Tutor, tutor_id=tutor_id)
    tutor.delete()
    return redirect('tutor_list')

def item_list(request):
    items = Item.objects.all()
    return render(request, 'sports_attandance/item_list.html', {'items': items})

# Create a new item
def item_create(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_list')  # Redirect to the item list page after saving
    else:
        form = ItemForm()
    return render(request, 'sports_attandance/item_form.html', {'form': form})

# Edit an existing item
def item_edit(request, item_id):
    item = get_object_or_404(Item, item_id=item_id)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm(instance=item)
    return render(request, 'sports_attandance/item_form.html', {'form': form})

# Delete an existing item
def item_delete(request, item_id):
    item = get_object_or_404(Item, item_id=item_id)
    item.delete()
    return redirect('item_list')



# List all student items
def student_item_list(request):
    student_items = StudentItem.objects.all()
    return render(request, 'sports_attandance/student_item_list.html', {'student_items': student_items})

# Create a new student-item entry
def student_item_create(request):
    if request.method == 'POST':
        form = StudentItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_item_list')  # Redirect to the list after saving
    else:
        form = StudentItemForm()
    return render(request, 'sports_attandance/student_item_form.html', {'form': form})

# Edit an existing student-item entry
def student_item_edit(request, stud_item_id):
    student_item = get_object_or_404(StudentItem, id=stud_item_id)
    if request.method == 'POST':
        form = StudentItemForm(request.POST, instance=student_item)
        if form.is_valid():
            form.save()
            return redirect('student_item_list')
    else:
        form = StudentItemForm(instance=student_item)
    return render(request, 'sports_attandance/student_item_form.html', {'form': form})

# Delete a student-item entry
def student_item_delete(request, stud_item_id):
    student_item = get_object_or_404(StudentItem, id=stud_item_id)
    student_item.delete()
    return redirect('student_item_list')

def hour_list(request):
    hours = Hour.objects.all()
    return render(request, 'sports_attandance/hour_list.html', {'hours': hours})

# Create a new hour entry (attendance record)
def hour_create(request):
    if request.method == 'POST':
        form = HourForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hour_list')  # Redirect to the list after saving
    else:
        form = HourForm()
    return render(request, 'sports_attandance/hour_form.html', {'form': form})

# Edit an existing hour entry (attendance record)
def hour_edit(request, hour_id):
    hour = get_object_or_404(Hour, id=hour_id)
    if request.method == 'POST':
        form = HourForm(request.POST, instance=hour)
        if form.is_valid():
            form.save()
            return redirect('hour_list')
    else:
        form = HourForm(instance=hour)
    return render(request, 'sports_attandance/hour_form.html', {'form': form})

# Delete an hour entry (attendance record)
def hour_delete(request, hour_id):
    hour = get_object_or_404(Hour, id=hour_id)
    hour.delete()
    return redirect('hour_list')


# List all present details (attendance records)
def present_details_list(request):
    present_details = PresentDetails.objects.all()
    return render(request, 'sports_attandance/present_details_list.html', {'present_details': present_details})

# Create a new attendance record (mark a student as present for a particular hour)
def present_details_create(request):
    if request.method == 'POST':
        form = PresentDetailsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('present_details_list')  # Redirect to the list after saving
    else:
        form = PresentDetailsForm()
    return render(request, 'sports_attandance/', {'form': form})

# Edit an existing attendance record
def present_details_edit(request, present_id):
    present_details = get_object_or_404(PresentDetails, id=present_id)
    if request.method == 'POST':
        form = PresentDetailsForm(request.POST, instance=present_details)
        if form.is_valid():
            form.save()
            return redirect('present_details_list')
    else:
        form = PresentDetailsForm(instance=present_details)
    return render(request, 'sports_attandance/present_details_form.html', {'form': form})

# Delete an attendance record
def present_details_delete(request, present_id):
    present_details = get_object_or_404(PresentDetails, id=present_id)
    present_details.delete()
    return redirect('present_details_list')


# List all statuses
def status_list(request):
    statuses = Status.objects.all()
    return render(request, 'sports_attandance/status_list.html', {'statuses': statuses})

# Create a new status
def status_create(request):
    if request.method == 'POST':
        form = StatusForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('status_list')  # Redirect to the list view after saving
    else:
        form = StatusForm()
    return render(request, 'sports_attandance/status_form.html', {'form': form})

# Edit an existing status
def status_edit(request, status_id):
    status = get_object_or_404(Status, id=status_id)
    if request.method == 'POST':
        form = StatusForm(request.POST, instance=status)
        if form.is_valid():
            form.save()
            return redirect('status_list')  # Redirect to the list view after saving
    else:
        form = StatusForm(instance=status)
    return render(request, 'sports_attandance/status_form.html', {'form': form})

# Delete a status
def status_delete(request, status_id):
    status = get_object_or_404(Status, id=status_id)
    status.delete()
    return redirect('status_list')  # Redirect to the list view after deleting

def student_list(request):
    students = Student.objects.all()  # Get all students
    return render(request, 'students/student_list.html', {'students': students})

# View to display a single student's details
def student_detail(request, stud_id):
    student = get_object_or_404(Student, stud_id=stud_id)
    return render(request, 'students/student_detail.html', {'student': student})

# View to create a new student
def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new student
            return redirect('student_list')  # Redirect to the student list
    else:
        form = StudentForm()  # Create an empty form
    return render(request, 'students/student_form.html', {'form': form})

# View to edit an existing student
def student_edit(request, stud_id):
    student = get_object_or_404(Student, stud_id=stud_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()  # Save the edited student
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)  # Populate the form with the existing student's data
    return render(request, 'students/student_form.html', {'form': form})

