# yourapp/templatetags/user_extras.py
from django import template
from employee.models import Employee

register = template.Library()

@register.filter
def is_manager(user):
    try:
        employee = Employee.objects.get(user=user)
        return employee.role == 'manager'
    except Employee.DoesNotExist:
        return False
