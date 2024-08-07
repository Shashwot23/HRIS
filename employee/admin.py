from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Employee, Department, Position

class EmployeeInline(admin.StackedInline):
    model = Employee
    can_delete = False

class CustomUserAdmin(UserAdmin):
    inlines = (EmployeeInline,)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Department)
admin.site.register(Position)