from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Goal, GoalRating, FunctionalArea, FunctionalAreaRating
from .forms import GoalForm, GoalRatingForm, FunctionalAreaRatingForm
from employee.models import Employee, Position, Department

@login_required
def performance(request):
    try:
        user_employee = Employee.objects.get(user=request.user)
    except Employee.DoesNotExist:
        user_employee = None
    

    if request.user.is_superuser:
        # For searchbar getting the ids
        department_id = request.GET.get('department')
        position_id = request.GET.get('position')
        search_name = request.GET.get('search_name')

        # getting employees form database
        employees = Employee.objects.all()
        positions = Position.objects.all()
        departments = Department.objects.all()

        # filtering for searchbar
        if department_id:
            employees = employees.filter(department_id=department_id)

        if position_id:
            employees = employees.filter(position_id=position_id)

        if search_name:
            employees = employees.filter(user__first_name__icontains=search_name) | employees.filter(user__last_name__icontains=search_name)


        context = {
            'employees': employees,
            'departments': departments,
            'positions': positions,
            'is_hr': True,
        }
    elif user_employee.role == 'manager':
        department_employees = Employee.objects.filter(department=user_employee.department)
        context = {
            'employees': department_employees,
            'is_manager':  True,
        }
    else:
        goals = Goal.objects.filter(employee=request.user)
        context = {
            'goals': goals,
            'is_employee': True,
        }
    return render(request, 'performance/performance.html', context)
    



@login_required
def set_goals_view(request):
    if request.method == 'POST':
        form = GoalForm(request.POST)
        if form.is_valid():
            goal = form.save(commit=False)
            goal.employee = request.user
            goal.save()
            return redirect('performance')
    else:
        form = GoalForm()
    return render(request, 'performance/set_goals.html',{'form':form})


@login_required
def approve_goals_view(request, employee_id):
    user_employee = Employee.objects.get(user=request.user)

    employee =get_object_or_404(Employee, id=employee_id, department=user_employee.department)

    goals = Goal.objects.filter(employee=employee.user)
    if request.method == 'POST':
        goal_id = request.POST.get('goal_id')
        goal = get_object_or_404(Goal, id=goal_id)
        goal.is_approved =True
        goal.save()
        return redirect('approve_goals', employee_id=employee_id)
    return render(request, 'performance/approve_goals.html', {'goals':goals})

@login_required
def rate_goals_view(request, employee_id):
    user_employee = Employee.objects.get(user=request.user)
    
    employee = get_object_or_404(Employee, id=employee_id, department=user_employee.department)
    goals = Goal.objects.filter(employee=employee.user, is_approved=True)


    if request.method =='POST':
        form = GoalRatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.rater = request.user
            rating.goal = get_object_or_404(Goal, id=request.POST.get('goal_id'))
            rating.save()
            return redirect('performance')
    else:
        form = GoalRatingForm()
    return render(request, 'performance/rate_goals.html', {'goals':goals, 'form':form, 'employee':employee})
    
@login_required
def rate_functional_areas_view(request, employee_id):
    user_employee = Employee.objects.get(user=request.user)
    employee = get_object_or_404(Employee, id=employee_id, department=user_employee.department)
    functional_areas = FunctionalArea.objects.all()

    if request.method == 'POST':
        ratings_data = request.POST.getlist('ratings')
        comments_data = request.POST.getlist('comments')

        for idx, functional_area in enumerate(functional_areas):
            rating_value = ratings_data[idx]
            comment_value = comments_data[idx]

            rating = FunctionalAreaRating(
                rater=request.user,
                employee=employee.user,
                functional_area=functional_area,
                rating=rating_value,
                comments=comment_value,
            )
            rating.save()

        return redirect('performance')

    return render(request, 'performance/rate_functional_areas.html', {'functional_areas': functional_areas, 'employee': employee})


@login_required
def view_employee_goals(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    goals = Goal.objects.filter(employee=employee.user, is_approved=True)
    ratings = GoalRating.objects.filter(goal__in=goals)
    performance = FunctionalAreaRating.objects.filter(employee=employee.user).select_related('employee', 'functional_area', 'rater')
    context = {
        'employee': employee,
        'goals': goals,
        'ratings': ratings,
        'performance': performance,
    }
    return render(request, 'performance/view_employee_goals.html', context)


