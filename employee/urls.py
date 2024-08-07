from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.employee_signup, name='employee_signup'),
    path('edit/<int:employee_id>/', views.edit_employee, name='edit_employee'),


]