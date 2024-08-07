from django.shortcuts import render, get_object_or_404
from employee.models import Employee, Department, Position
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from calender.models import Events
from django.contrib.auth.decorators import user_passes_test
from .models import Task, Announcement
from .forms import TaskAssignmentForm, AnnouncementForm

# Create your views here.
@login_required
def dashboard(request):
    user = request.user
    events = Events.objects.all().order_by('start')
    tasks = Task.objects.filter(assigned_to=request.user, completed=False)
    announcements = Announcement.objects.all().order_by('-created_at')
    if user.is_superuser:
        employee_count = Employee.objects.all().count()
        departments = Department.objects.all()
        department_names = [dept.name for dept in departments]
        headcounts = [Employee.objects.filter(department=dept).count() for dept in departments]

        context={
            'is_superuser': True,
            'user': user,
            'events': events,
            'department_names': department_names,
            'headcounts': headcounts,
            'employee_count': employee_count,
            'announcements': announcements,
        }
    else:
        employee = get_object_or_404(Employee, user=user)
        context = {
            'is_superuser': False,
            'employee': employee,
            'events': events,
            'tasks':tasks,
            'announcements': announcements
        }
    return render(request, 'dashboard/dashboard.html', context)


def employee_list(request):
    # For searchbar getting the ids
    department_id = request.GET.get('department')
    position_id = request.GET.get('position')
    search_name = request.GET.get('search_name')

    try:
        user_employee = Employee.objects.get(user=request.user)
    except Employee.DoesNotExist:
        user_employee = None


    if user_employee and user_employee.role == 'manager':
        employees = Employee.objects.filter(department=user_employee.department)
        # Filter positions based on the manager's department
        positions = Position.objects.filter(department=user_employee.department)
    else:
        employees = Employee.objects.all()
        # Show all positions for superuser or general users
        positions = Position.objects.all()

    if department_id:
        employees = employees.filter(department_id=department_id)

    if position_id:
        employees = employees.filter(position_id=position_id)

    if search_name:
        employees = employees.filter(user__first_name__icontains=search_name) | employees.filter(user__last_name__icontains=search_name)

    departments = Department.objects.all()
    # positions = Position.objects.all()

    context = {
        'employees': employees,
        'departments': departments,
        'positions': positions,
        'user_employee': user_employee, 
    }

    return render(request, 'dashboard/employee_list.html', context)

def performance(request):
    return render(request, 'performance/performance.html')

def logout_view(request):
    logout(request)
    return redirect('login')


def assign_task(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    if request.method == 'POST':
        form = TaskAssignmentForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.assigned_to = employee.user
            task.assigned_by = request.user
            task.save()
            return redirect('employee_list')
    else:
        form = TaskAssignmentForm()
    return render(request, 'dashboard/assign_task.html', {'form':form, 'employee':employee})

@login_required
def create_announcement(request):
    if request.method == 'POST':
        form = AnnouncementForm(request.POST)
        if form.is_valid():
            announcement = form.save(commit=False)
            announcement.created_by = request.user
            announcement.save()
            return redirect('dashboard')
    else:
        form = AnnouncementForm()
    
    return render(request, 'dashboard/create_announcement.html', {'form': form})