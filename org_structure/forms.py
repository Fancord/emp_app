from django.forms import ModelForm

from .models import Employee


class EmployeeForm(ModelForm):
    """Для создания танца на сайте"""
    class Meta:
        model = Employee
        fields = ['fio', 'position', 'department', 'first_day']