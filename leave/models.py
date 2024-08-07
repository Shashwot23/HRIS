from django.db import models
from django.contrib.auth.models import User
from employee.models import Employee

# Create your models here.

class LeaveType(models.Model):
    name = models.CharField(max_length=50)
    discription = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class LeaveRequest(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]

    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    leave_type = models.ForeignKey(LeaveType, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    supervisor_comments = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.employee.first_name} - {self.leave_type} ({self.status})"
    
