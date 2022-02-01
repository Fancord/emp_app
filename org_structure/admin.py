from django.contrib import admin

from .models import Employee, Department, Position


class EmployeeAdmin(admin.ModelAdmin):
    exclude = ('worked_time',)
    list_display = ('fio', 'position', 'department', 'first_day', 'worked_time')


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Department)
admin.site.register(Position)

