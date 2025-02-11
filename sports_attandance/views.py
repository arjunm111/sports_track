# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Department,Programme
from .forms import DepartmentForm,ProgrammeForm
from django.http import HttpResponse


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
            return redirect('department_list')  # Redirect to the department list after editing
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