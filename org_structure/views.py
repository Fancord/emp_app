from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import EmployeeForm
from .models import Position, Employee, Department


@login_required
def home_page(request):
    return render(request, 'org_structure/home_page.html')


"""Регистрация пользователя"""


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', context={'form': form})


"""Должности"""


class PositionModelViewSet(LoginRequiredMixin, ListView):
    """Справочник должностей"""
    model = Position
    queryset = Position.objects.all()
    template_name = "org_structure/positions.html"


"""Сотрудники"""


class EmployeeModelViewSet(LoginRequiredMixin, ListView):
    """Список должностей"""
    model = Employee
    queryset = Employee.objects.all()
    template_name = "org_structure/employees.html"


class EmployeeDetailView(LoginRequiredMixin, DetailView):
    """Карточка сотрудника"""
    model = Employee
    queryset = Employee.objects.all()
    slug_field = 'fio'
    template_name = "org_structure/employee_detail.html"


class EmployeeCreate(LoginRequiredMixin, CreateView):
    """
    Создания модели сотрудника
    """
    template_name = 'org_structure/employee_form.html'
    form_class = EmployeeForm
    success_url = reverse_lazy('employees')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Employee'] = Employee.objects.all()
        return context


class EmployeeUpdate(LoginRequiredMixin, UpdateView):
    """
    Изменение модели сотрудника
    """
    template_name = 'org_structure/employee_form.html'
    model = Employee
    fields = ['fio', 'position', 'department', 'first_day']
    success_url = reverse_lazy('employees')


class EmployeeDelete(LoginRequiredMixin, DeleteView):
    """
    Удаление модели сотрудника
    """
    template_name = 'org_structure/employee_delete.html'
    model = Employee
    success_url = reverse_lazy('employees')


"""Отделы"""


class DepartmentModelViewSet(LoginRequiredMixin, ListView):
    """Справочник отделов"""
    model = Department
    queryset = Department.objects.all()
    template_name = "org_structure/departments.html"


class DepartmentCreate(LoginRequiredMixin, CreateView):
    model = Department
    fields = '__all__'
    template_name = "org_structure/department_form.html"
    success_url = reverse_lazy('departments')


class DepartmentUpdate(LoginRequiredMixin, UpdateView):
    model = Department
    fields = '__all__'
    template_name = "org_structure/department_form.html"
    success_url = reverse_lazy('departments')


class DepartmentDelete(LoginRequiredMixin, DeleteView):
    model = Department
    success_url = reverse_lazy('departments')
    template_name = "org_structure/department_delete.html"
