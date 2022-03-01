from django.contrib import admin

from .models import Worker, Department


class WorkerAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        """
        getting queryset for all Worker objects
        """
        queryset = Worker.objects_all.all()
        if not self.has_view_or_change_permission(request):
            queryset = queryset.none()
        return queryset

    list_display = (
        'id',
        'first_name',
        'last_name',
        'startwork_date',
        'tab_num',
        'department',
    )


class DepartmentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
    )


admin.site.register(Worker, WorkerAdmin)
admin.site.register(Department, DepartmentAdmin)