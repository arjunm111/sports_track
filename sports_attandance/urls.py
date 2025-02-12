

from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_view, name='home'),
    path('list/', views.department_list, name='department_list'),  # View to display the department list
    path('create/', views.department_create, name='department_create'),  # View to create a new department
    path('edit/<int:dept_id>/', views.department_edit, name='department_edit'),  # View to edit an existing department
    path('delete/<int:dept_id>/', views.department_delete, name='department_delete'),  # View to delete a department
    path('programmes/', views.programme_list, name='programme_list'),  # View all programmes
    path('programmes/create/', views.programme_create, name='programme_create'),  # Create a new programme
    path('programmes/edit/<int:pgm_id>/', views.programme_edit, name='programme_edit'),  # Edit a programme
    path('programmes/delete/<int:pgm_id>/', views.programme_delete, name='programme_delete'),  # Delete a programme
    path('teachers/', views.teacher_list, name='teacher_list'),  # List all teachers
    path('teachers/create/', views.teacher_create, name='teacher_create'),  # Create a new teacher
    path('teachers/edit/<int:teacher_id>/', views.teacher_edit, name='teacher_edit'),
    path('teachers/delete/<int:teacher_id>/', views.teacher_delete, name='teacher_delete'),  # Delete a teacher
    path('tutors/', views.tutor_list, name='tutor_list'),  # List all tutors
    path('tutors/create/', views.tutor_create, name='tutor_create'),  # Create a new tutor
    path('tutors/edit/<int:tutor_id>/', views.tutor_edit, name='tutor_edit'),  # Edit a tutor
    path('tutors/delete/<int:tutor_id>/', views.tutor_delete, name='tutor_delete'),  # Delete a tutor
    path('items/', views.item_list, name='item_list'),  # List all items
    path('item/create/', views.item_create, name='item_create'),  # Create a new item
    path('item/edit/<int:item_id>/', views.item_edit, name='item_edit'),  # Edit an item
    path('item/delete/<int:item_id>/', views.item_delete, name='item_delete'),  # Delete an item
    path('student-items/', views.student_item_list, name='student_item_list'),  # List all student-items
    path('student-item/create/', views.student_item_create, name='student_item_create'),  # Create a new student-item
    path('student-item/edit/<int:stud_item_id>/', views.student_item_edit, name='student_item_edit'),  # Edit a student-item
    path('student-item/delete/<int:stud_item_id>/', views.student_item_delete, name='student_item_delete'),  # Delete a student-item
    path('hours/', views.hour_list, name='hour_list'),  # List all hours
    path('hour/create/', views.hour_create, name='hour_create'),  # Create new hour entry
    path('hour/edit/<int:hour_id>/', views.hour_edit, name='hour_edit'),  # Edit an hour entry
    path('hour/delete/<int:hour_id>/', views.hour_delete, name='hour_delete'),  # Delete an hour entry
    path('present_details/', views.present_details_list, name='present_details_list'),  # List all present details
    path('present_details/create/', views.present_details_create, name='present_details_create'),  # Create new present details
    path('present_details/edit/<int:present_id>/', views.present_details_edit, name='present_details_edit'),  # Edit present details
    path('present_details/delete/<int:present_id>/', views.present_details_delete, name='present_details_delete'),  # Delete present details
    path('status/', views.status_list, name='status_list'),  # List all statuses
    path('status/create/', views.status_create, name='status_create'),  # Create new status
    path('status/edit/<int:status_id>/', views.status_edit, name='status_edit'),  # Edit status
    path('status/delete/<int:status_id>/', views.status_delete, name='status_delete'),  # Delete status
    path('student', views.student_list, name='student_list'),  # List all students
    path('student/create/', views.student_create, name='student_create'),  # Create a new student
    path('student/edit/<int:stud_id>/', views.student_edit, name='student_edit'),  # Edit a student
    path('student/details/<int:stud_id>/', views.student_detail, name='student_detail'),  # View student details
    path('request/create/', views.create_request, name='create_request'),  # For creating a new request
    path('request/', views.request_list, name='request_list'),  # To view all requests
    path('request/edit/<int:request_id>/', views.edit_request, name='edit_request'),  # For editing a request
]

