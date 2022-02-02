from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import EmployeeModelViewSet, EmployeeDetailView, PositionModelViewSet, home_page, EmployeeCreate, \
    EmployeeUpdate, EmployeeDelete, DepartmentCreate, DepartmentModelViewSet, DepartmentUpdate, DepartmentDelete, \
    register

"""Общие urls"""

urlpatterns = [
    path('', home_page, name='home_page'),
    path('register/', register, name='register'),
]

"""Positions urls"""
urlpatterns += [
    path('positions/', PositionModelViewSet.as_view(), name='positions'),
]

"""Employees urls"""
urlpatterns += [
    path('add/employees/', EmployeeCreate.as_view(), name='employee_add'),
    path('employees/', EmployeeModelViewSet.as_view(), name='employees'),
    path('employees/<str:slug>/', EmployeeDetailView.as_view(), name='employee_detail'),
    path('employees/<int:pk>/update', EmployeeUpdate.as_view(), name='employee_update'),
    path('employees/<int:pk>/delete', EmployeeDelete.as_view(), name='employee_delete'),
]

"""Department urls"""
urlpatterns += [
    path('add/department/', DepartmentCreate.as_view(), name='department_add'),
    path('departments/', DepartmentModelViewSet.as_view(), name='departments'),
    path('departments/<int:pk>/update', DepartmentUpdate.as_view(), name='department_update'),
    path('departments/<int:pk>/delete', DepartmentDelete.as_view(), name='department_delete'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
