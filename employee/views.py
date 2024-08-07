# views.py
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect, get_object_or_404
from .forms import EmployeeCreationForm
from .models import Employee

def employee_signup(request):
    #if not request.user.is_superuser:
    #    return redirect('dashboard')  # Only superuser can access signup
    if request.method == 'POST':
        form = EmployeeCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def employee_signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})


def edit_employee(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    user = employee.user
    
    if request.method == 'POST':
        if 'delete' in request.POST:
            employee.delete()
            return redirect('employee_list')  # Redirect to employee list or other view
        else:
            form = EmployeeCreationForm(request.POST, instance=user, employee_instance=employee)
            if form.is_valid():
                form.save()
                return redirect('employee_list')  # Redirect to employee list or detail view
    else:
        form = EmployeeCreationForm(instance=user, employee_instance=employee)
    
    return render(request, 'registration/edit_employee.html', {'form': form, 'employee': employee})