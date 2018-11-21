from django.contrib import admin
from testapp.models import *
# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id','E_NO','E_NAME','E_SAL','E_ADDRESS']

admin.site.register(Employee,EmployeeAdmin)
