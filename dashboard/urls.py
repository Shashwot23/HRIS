from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('employee_list', views.employee_list, name='employee_list'),
    path('performance', views.performance, name='performance'),
    path('logout', views.logout_view, name='logout'),
    path('assign-task/<int:employee_id>/', views.assign_task, name='assign_task'),
    path('create/', views.create_announcement, name='create_announcement'),

]