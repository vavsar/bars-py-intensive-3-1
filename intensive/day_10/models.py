from django.db import models


class Department(models.Model):
    """
    Подразделение
    """
    name = models.CharField('Наименование', max_length=30)


class Worker(models.Model):
    """
    Сотрудник
    """
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    tab_num = models.IntegerField('Табельный номер', default=0)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='workers')
