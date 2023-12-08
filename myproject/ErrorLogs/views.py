from django.shortcuts import render
from .models import Errors, Programmers, ErrorFixes


def error_logs_view(request):
    errors = Errors.objects.all()
    programmers = Programmers.objects.all()
    error_fixes = ErrorFixes.objects.all()

    return render(request, 'ErrorLogs/error_logs.html', {
        'errors': errors,
        'programmers': programmers,
        'error_fixes': error_fixes
    })
