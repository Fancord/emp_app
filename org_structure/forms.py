from django import forms

from .models import Employee


class EmployeeForm(forms.ModelForm):
    """Для создания танца на сайте"""
    class Meta:
        model = Employee
        fields = ['fio', 'position', 'department', 'first_day']
