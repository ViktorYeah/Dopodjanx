from django.contrib import admin
from .models import CompanyInfo

@admin.register(CompanyInfo)
class PostAdmin(admin.ModelAdmin):
    list_display = ('Id', 'Name', 'DateTime', 'Employees', 'Assets', 'Link')