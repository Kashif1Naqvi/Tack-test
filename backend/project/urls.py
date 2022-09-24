from app.views import daily_performance, filter_by_min_roi
from django.contrib import admin
from django.urls import path
urlpatterns = [
    path('daily_performance/', daily_performance),
    path('filter_by_min_roi/', filter_by_min_roi),
    path('admin/', admin.site.urls)
]
