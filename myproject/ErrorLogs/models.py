from django.db import models


class Errors(models.Model):
    ERROR_LEVEL_CHOICES = [
        ('Critical', 'Critical'),
        ('Important', 'Important'),
        ('Minor', 'Minor'),
    ]
    CATEGORY_CHOICES = [
        ('Interface', 'Interface'),
        ('Data', 'Data'),
        # Add other categories
    ]
    SOURCE_CHOICES = [
        ('User', 'User'),
        ('Tester', 'Tester'),
        # Add other sources
    ]
    error_code = models.CharField(max_length=100)
    description = models.TextField()
    reception_date = models.DateField()
    error_level = models.CharField(max_length=10, choices=ERROR_LEVEL_CHOICES)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    source = models.CharField(max_length=50, choices=SOURCE_CHOICES)


class Programmers(models.Model):
    programmer_code = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)


class ErrorFixes(models.Model):
    FIX_DURATION_CHOICES = [
        ('1 day', '1 day'),
        ('2 days', '2 days'),
        # Add other durations
    ]
    fix_code = models.CharField(max_length=100)
    error = models.ForeignKey(Errors, on_delete=models.CASCADE)
    start_date = models.DateField()
    fix_duration = models.CharField(max_length=10, choices=FIX_DURATION_CHOICES)
    programmer = models.ForeignKey(Programmers, on_delete=models.CASCADE)
    cost_per_day = models.DecimalField(max_digits=10, decimal_places=2)
