from django.contrib import admin
from django.urls import path, include
from users.views import login_view, register_view

urlpatterns = [
    path('auth/', include('users.urls')),
    path('admin/', admin.site.urls),
]
