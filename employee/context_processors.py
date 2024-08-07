# context_processors.py
from .models import Employee

def employee_context(request):
    if request.user.is_authenticated:
        try:
            user_employee = Employee.objects.get(user=request.user)
        except Employee.DoesNotExist:
            user_employee = None
    else:
        user_employee = None
    return {'user_employee': user_employee}
