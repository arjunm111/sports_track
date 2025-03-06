from django.shortcuts import render, redirect, get_object_or_404
from .models import Department, Programme, Student, Item,Teacher,Tutor
from .forms import DepartmentForm, ProgrammeForm, StudentForm, ItemForm,TeacherForm,TutorForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def landing(request):
    return render(request, 'sports_attendance/landing.html')
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            
            if user.is_superuser:  # Admin login
                return redirect('admin_dashboard')

            try:
                teacher = Teacher.objects.get(user_id=user)
                if teacher.is_hod:
                    return redirect('hod_dashboard')  # Redirect HODs
                else:
                    return redirect('index_teacher')  # Redirect normal teachers
            except Teacher.DoesNotExist:
                return render(request, 'sports_attendance/login.html', {'error': 'Unauthorized access'})  

        else:
            return render(request, 'sports_attendance/login.html', {'error': 'Invalid username or password'})

    return render(request, 'sports_attendance/login.html')



def user_logout(request):
    logout(request)
    request.session.flush()  # Clear session data
    return redirect("login")  # Redirect to login page after logout
@login_required
def dashboard_view(request):
    if request.user.is_superuser:  # Admin dashboard
        return render(request, 'sports_attendance/admin_dashboard.html')
    else:
        try:
            # Get the teacher object based on the logged-in user
            teacher = Teacher.objects.get(user_id=request.user)
            # Fetch the courses assigned to this teacher
            return render(request, 'sports_attendance/user_dashboard.html')
        except Teacher.DoesNotExist:
            # Handle if the logged-in user is not a teacher (maybe a regular user)
            return redirect('user_dashboard')  # Or any appropriate action for non-teachers



# Manage Departments
def department_list(request):
    departments = Department.objects.all()
    return render(request, 'sports_attendance/department_list.html', {'departments': departments})

def department_create(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('department_list')
    else:
        form = DepartmentForm()
    return render(request, 'sports_attendance/department_form.html', {'form': form})

def department_update(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            return redirect('department_list')
    else:
        form = DepartmentForm(instance=department)
    return render(request, 'sports_attendance/department_form.html', {'form': form})



# Manage Programmes
def programme_list(request):
    programmes = Programme.objects.all()
    return render(request, 'sports_attendance/programme_list.html', {'programmes': programmes})

def programme_create(request):
    if request.method == 'POST':
        form = ProgrammeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('programme_list')
    else:
        form = ProgrammeForm()
    return render(request, 'sports_attendance/programme_form.html', {'form': form})

def programme_update(request, pk):
    programme = get_object_or_404(Programme, pk=pk)
    if request.method == 'POST':
        form = ProgrammeForm(request.POST, instance=programme)
        if form.is_valid():
            form.save()
            return redirect('programme_list')
    else:
        form = ProgrammeForm(instance=programme)
    return render(request, 'sports_attendance/programme_form.html', {'form': form})



# Manage Students
def student_list(request):
    students = Student.objects.all()
    return render(request, 'sports_attendance/student_list.html', {'students': students})

def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'sports_attendance/student_form.html', {'form': form})

def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'sports_attendance/student_form.html', {'form': form})

def item_list(request):
    items = Item.objects.all()
    return render(request, 'sports_attendance/item_list.html', {'items': items})

# Create a new item
def item_create(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm()
    return render(request, 'sports_attendance/item_form.html', {'form': form, 'title': 'Add Item'})

# Update an existing item
def item_update(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm(instance=item)
    return render(request, 'sports_attendance/item_form.html', {'form': form, 'title': 'Edit Item'})

# Delete an item
#def item_delete(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('item_list')
    return render(request, 'items/item_confirm_delete.html', {'item': item})
# List all teachers
def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'sports_attendance/teacher_list.html', {'teachers': teachers})

# View details of a teacher
def teacher_detail(request, teacher_id):
    teacher = get_object_or_404(Teacher, teacher_id=teacher_id)
    return render(request, 'sports_attendance/teacher_detail.html', {'teacher': teacher})

# Add a new teacher
def teacher_create(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teacher_list')
    else:
        form = TeacherForm()
    return render(request, 'sports_attendance/teacher_form.html', {'form': form})

# Update an existing teacher
def teacher_update(request, teacher_id):
    teacher = get_object_or_404(Teacher, teacher_id=teacher_id)
    if request.method == 'POST':
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('teacher_list')
    else:
        form = TeacherForm(instance=teacher)
    return render(request, 'sports_attendance/teacher_form.html', {'form': form})

# Delete a teacher
def teacher_delete(request, teacher_id):
    teacher = get_object_or_404(Teacher, teacher_id=teacher_id)
    teacher.delete()
    return redirect('teacher_list')

# List all tutors
def tutor_list(request):
    tutors = Tutor.objects.all()
    return render(request, 'sports_attendance/tutor_list.html', {'tutors': tutors})

# View tutor details
def tutor_detail(request, tutor_id):
    tutor = get_object_or_404(Tutor, tutor_id=tutor_id)
    return render(request, 'sports_attendance/tutor_detail.html', {'tutor': tutor})

# Create tutor
def tutor_create(request):
    if request.method == 'POST':
        form = TutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tutor_list')
    else:
        form = TutorForm()
    return render(request, 'sports_attendance/tutor_form.html', {'form': form})

# Update tutor
def tutor_update(request, tutor_id):
    tutor = get_object_or_404(Tutor, tutor_id=tutor_id)
    if request.method == 'POST':
        form = TutorForm(request.POST, instance=tutor)
        if form.is_valid():
            form.save()
            return redirect('tutor_list')
    else:
        form = TutorForm(instance=tutor)
    return render(request, 'sports_attendance/tutor_form.html', {'form': form})

# Delete tutor
def tutor_delete(request, tutor_id):
    tutor = get_object_or_404(Tutor, tutor_id=tutor_id)
    tutor.delete()
    return redirect('tutor_list')