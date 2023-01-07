from django.contrib import admin
from .models import Employee, Role, Department

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "hire_date")

admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Role)
admin.site.register(Department)


# Register your models here.
