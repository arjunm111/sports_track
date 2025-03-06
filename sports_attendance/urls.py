from django.urls import path
from . import views 
from .views import login_view, user_logout

urlpatterns = [
    
    path('', views.landing, name='landing'),
    path("login/", login_view, name="login"),
    path("logout/", user_logout, name="logout"),
    path('admin-dashboard/', views.dashboard_view, name='admin_dashboard'),
    path('students/', views.student_list, name='student_list'),
    path('students/create/', views.student_create, name='student_create'),
    path('students/update/<int:pk>/', views.student_update, name='student_update'),
    #path('students/delete/<int:pk>/', views.student_delete, name='student_delete'),

    path('departments/', views.department_list, name='department_list'),
    path('departments/create/', views.department_create, name='department_create'),
    path('departments/update/<int:pk>/', views.department_update, name='department_update'),
    #path('departments/delete/<int:pk>/', views.department_delete, name='department_delete'),

    path('programmes/', views.programme_list, name='programme_list'),
    path('programmes/create/', views.programme_create, name='programme_create'),
    path('programmes/update/<int:pk>/', views.programme_update, name='programme_update'),
    #path('programmes/delete/<int:pk>/', views.programme_delete, name='programme_delete'),

    path('items/', views.item_list, name='item_list'),
    path('items/create/', views.item_create, name='item_create'),
    path('items/update/<int:pk>/', views.item_update, name='item_update'),
    
    #path('items/delete/<int:pk>/', views.item_delete, name='item_delete'),

   
    path('teachers/', views.teacher_list, name='teacher_list'),
    path('teachers/create/', views.teacher_create, name='teacher_create'),
    path('teachers/update/<int:teacher_id>/', views.teacher_update, name='teacher_update'),
    path('teachers/delete/<int:teacher_id>/', views.teacher_delete, name='teacher_delete'),

    # Tutor URLs
    path('tutors/', views.tutor_list, name='tutor_list'),
    path('tutors/create/', views.tutor_create, name='tutor_create'),
    path('tutors/update/<int:tutor_id>/', views.tutor_update, name='tutor_update'),
    path('tutors/delete/<int:tutor_id>/', views.tutor_delete, name='tutor_delete'),
]


