from django.urls import path
from . import views


urlpatterns = [
    path('', views.performance, name='performance'),
    path('set/', views.set_goals_view, name='set_goals'),
    path('approve/<int:employee_id>', views.approve_goals_view, name='approve_goals'),
    path('rate/<int:employee_id>/', views.rate_goals_view, name='rate_goals'),
    path('rate-functional-areas/<int:employee_id>/', views.rate_functional_areas_view, name='rate_functional_areas'),
    path('employee/<int:employee_id>/goals/', views.view_employee_goals, name='view_employee_goals'),  # New URL pattern
]