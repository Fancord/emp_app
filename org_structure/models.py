import datetime

from django.db import models
from django.utils import timezone


class Position(models.Model):
    """Модель позиций"""
    name = models.CharField(max_length=126, unique=True, verbose_name='Position name')


class Department(models.Model):
    """Модель департаментов"""
    name = models.CharField(max_length=126, unique=True, verbose_name='Department name')


class Employee(models.Model):
    """Модель сотрудника"""
    fio = models.CharField(max_length=100, unique=True, verbose_name='Full name')
    position = models.ForeignKey(Position, on_delete=models.SET_NULL)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL)
    first_day = models.DateField(default=timezone.now, verbose_name='First day')
    worked_time = models.IntegerField(blank=True, verbose_name='Worked time')

    def years_of_work(self):
        """Получение кол-во лет работы сотрудника"""
        return datetime.date.today().year - self.first_day.year

    def save(self, *args, **kwargs):
        """Перегрузка метода для сохранения кол-ва лет работы сотрудника"""
        self.worked_time = self.years_of_work()
        super(Employee, self).save(*args, **kwargs)
