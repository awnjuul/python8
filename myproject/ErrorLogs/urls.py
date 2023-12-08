from django.urls import path
from . import views

app_name = 'ErrorLogs'

urlpatterns = [
    path('error_logs/', views.error_logs_view, name='error_logs_view'),
]
