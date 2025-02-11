

from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_view, name='home'),
    path('list/', views.department_list, name='department_list'),  # View to display the department list
    path('create/', views.department_create, name='department_create'),  # View to create a new department
    path('edit/<int:dept_id>/', views.department_edit, name='department_edit'),  # View to edit an existing department
    path('delete/<int:dept_id>/', views.department_delete, name='department_delete'),  # View to delete a department
    path('programmes/', views.programme_list, name='programme_list'),  # View all programmes
    path('programme/create/', views.programme_create, name='programme_create'),  # Create a new programme
    path('programme/edit/<int:pgm_id>/', views.programme_edit, name='programme_edit'),  # Edit a programme
    path('programme/delete/<int:pgm_id>/', views.programme_delete, name='programme_delete'),  # Delete a programme
]
