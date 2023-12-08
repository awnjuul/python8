from django.contrib import admin
from django.urls import path, include
from ErrorLogs import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('errorlogs/', views.error_logs_view),
]
