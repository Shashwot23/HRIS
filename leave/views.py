from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import LeaveRequest, LeaveType
from .forms import LeaveRequestForm
from django.contrib.auth.models import User

@login_required
def leave_home(request):
    user = request.user
    if user.is_superuser:
        leave_requests = LeaveRequest.objects.all() 
        context={
                'is_superuser': True,
                'user': user,
                'leave_requests': leave_requests,
            }
    else:
        employee = request.user
        leave_requests = LeaveRequest.objects.filter(employee=employee)
        context={
            'is_superuser': False,
            'employee': employee,
            'leave_requests': leave_requests,
            
        }
    return render(request, 'leave/leave_home.html',context)


@login_required
def apply_leave(request):
    if request.method == 'POST':
        form = LeaveRequestForm(request.POST)
        if form.is_valid():
            leave_request = form.save(commit=False)
            leave_request.employee = request.user
            leave_request.save()
            return redirect('leave')
    else:
        form = LeaveRequestForm()
    return render(request, 'leave/apply_leave.html', {'form': form})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def manage_leave_requests(request):
    leave_requests = LeaveRequest.objects.all()
    return render(request, 'leave/manage_leave.html', {'leave_requests': leave_requests})


@login_required
@user_passes_test(lambda u: u.is_superuser)
def approve_leave_request(request, pk):
    leave_request = get_object_or_404(LeaveRequest, pk=pk)
    leave_request.status = 'Approved'
    leave_request.save()
    return redirect('leave')

@login_required
@user_passes_test(lambda u: u.is_superuser)
def reject_leave_request(request, pk):
    leave_request = get_object_or_404(LeaveRequest, pk=pk)
    leave_request.status = 'Rejected'
    leave_request.save()
    return redirect('leave')