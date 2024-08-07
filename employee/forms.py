from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils import timezone
from .models import Employee, Department, Position

class EmployeeCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    department = forms.ModelChoiceField(queryset=Department.objects.all())
    position = forms.ModelChoiceField(queryset=Position.objects.all())
    role = forms.ChoiceField(choices=Employee.ROLE_CHOICES, required=True)
    date_of_birth = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    phone_number = forms.CharField(max_length=15, required=False)
    address = forms.CharField(widget=forms.Textarea, required=False)
    

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        self.employee_instance = kwargs.pop('employee_instance', None)
        super(EmployeeCreationForm, self).__init__(*args, **kwargs)

        if self.employee_instance:
            self.fields['department'].initial = self.employee_instance.department
            self.fields['position'].initial = self.employee_instance.position
            self.fields['date_of_birth'].initial = self.employee_instance.date_of_birth
            self.fields['phone_number'].initial = self.employee_instance.phone_number
            self.fields['address'].initial = self.employee_instance.address
            self.fields['role'].initial = self.employee_instance.role

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            if self.employee_instance:
                employee = self.employee_instance
            else:
                employee = Employee(user=user)
            
            employee.department = self.cleaned_data['department']
            employee.position = self.cleaned_data['position']
            employee.role = self.cleaned_data['role']
            employee.date_of_birth = self.cleaned_data['date_of_birth']
            employee.phone_number = self.cleaned_data['phone_number']
            employee.address = self.cleaned_data['address']
            if not employee.date_hired:
                employee.date_hired = timezone.now().date()
            
            employee.save()
        return user
