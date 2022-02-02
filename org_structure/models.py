import datetime

from django.db import models
from django.utils import timezone
from django.utils.text import slugify


class Position(models.Model):
    """Модель должности"""
    name = models.CharField(max_length=126, unique=True, verbose_name='Position name')
    description = models.TextField(blank=True, verbose_name='Description of position')
    slug = models.SlugField(max_length=150, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Position, self).save(*args, **kwargs)


class Department(models.Model):
    """Модель отдела"""
    name = models.CharField(max_length=126, unique=True, verbose_name='Department name')
    description = models.TextField(blank=True, verbose_name='Description of department')
    slug = models.SlugField(max_length=150, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Department, self).save(*args, **kwargs)


class Employee(models.Model):
    """Модель сотрудника"""
    fio = models.CharField(max_length=100, unique=True, verbose_name='Full name')
    position = models.ForeignKey(Position, null=True, on_delete=models.SET_NULL)
    department = models.ForeignKey(Department, null=True, on_delete=models.SET_NULL)
    first_day = models.DateField(default=timezone.now, verbose_name='First day')
    worked_time = models.IntegerField(blank=True, verbose_name='Worked time')

    def years_of_work(self):
        """Получение кол-во лет работы сотрудника"""
        return datetime.date.today().year - self.first_day.year

    def save(self, *args, **kwargs):
        """Перегрузка метода для сохранения кол-ва лет работы сотрудника"""
        self.worked_time = self.years_of_work()
        super(Employee, self).save(*args, **kwargs)

    def __str__(self):
        return self.fio

