# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.leave_home, name='leave'),
    path('apply-leave/', views.apply_leave, name='apply_leave'),
    path('manage-leave-requests/', views.manage_leave_requests, name='manage_leave_requests'),
    path('approve-leave-request/<int:pk>/', views.approve_leave_request, name='approve_leave_request'),
    path('reject-leave-request/<int:pk>/', views.reject_leave_request, name='reject_leave_request'),
]
