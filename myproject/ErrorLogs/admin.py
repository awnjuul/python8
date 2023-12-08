from django.contrib import admin
from ErrorLogs.models import Errors, Programmers, ErrorFixes

# Register your models here.
admin.site.register(Errors)
admin.site.register(Programmers)
admin.site.register(ErrorFixes)


# @admin.register(Errors)
# class ErrorsAdmin(admin.ModelAdmin):
#     list_display = ('error_code', 'description', 'reception_date', 'error_level', 'category', 'source')
#     list_filter = ('error_level', 'category', 'source')
#     search_fields = ('error_code', 'description')
#
#
# @admin.register(Programmers)
# class ProgrammersAdmin(admin.ModelAdmin):
#     list_display = ('programmer_code', 'name', 'phone_number')
#     search_fields = ('name',)
#
#
# @admin.register(ErrorFixes)
# class ErrorFixesAdmin(admin.ModelAdmin):
#     list_display = ('fix_code', 'error', 'start_date', 'fix_duration', 'programmer', 'cost_per_day')
#     list_filter = ('start_date', 'fix_duration')
#     search_fields = ('fix_code',)
