from django.contrib import admin

from .models import OrderedWorker


class OrderedWorkerAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'startwork_date',
    )


admin.site.register(OrderedWorker, OrderedWorkerAdmin)
