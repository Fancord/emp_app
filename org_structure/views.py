from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView

from .forms import EmployeeForm
from .models import Position, Employee


def home_page(request):
    return render(request, 'home_page.html')


class PositionModelViewSet(ListView):
    """Справочник должностей"""
    model = Position
    queryset = Position.objects.all()
    template_name = "positions.html"


class EmployeeModelViewSet(ListView):
    """Справочник должностей"""
    model = Employee
    queryset = Employee.objects.all()
    template_name = "employees.html"


class EmployeeDetailView(DetailView):
    """Справочник должностей"""
    model = Employee
    queryset = Employee.objects.all()
    slug_field = 'fio'
    template_name = "employee_detail.html"


class EmployeeCreateView(CreateView):
    """
    Создания модели сотрудника
    """
    template_name = 'create_employee.html'
    form_class = EmployeeForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Employee'] = Employee.objects.all()
        return context

