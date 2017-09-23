from django.contrib import admin
from .models import Standup, Company


class StandupAdmin(admin.ModelAdmin):
    list_display = ['yesterday', 'today', 'blocker',
                    'user', 'timestamp', 'updated']


class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'timestamp', 'updated']

# Register your models here.
admin.site.register(Standup, StandupAdmin)
admin.site.register(Company, CompanyAdmin)


