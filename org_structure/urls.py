from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import EmployeeModelViewSet, EmployeeDetailView, PositionModelViewSet, home_page, EmployeeCreateView

urlpatterns = [
    path('', home_page, name='home_page'),
    path('employees/', EmployeeModelViewSet.as_view(), name='employees'),
    path('employees/<str:slug>/', EmployeeDetailView.as_view(), name='employees_detail'),
    path('add/employees/', EmployeeCreateView.as_view(), name='add_employee'),
    path('positions/', PositionModelViewSet.as_view(), name='positions'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
