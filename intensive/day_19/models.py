from django.db import models


class Worker(models.Model):
    """
    Модель работника
    """

    fio = models.CharField('ФИО', max_length=127)

    class Meta:
        db_table = 'worker'
