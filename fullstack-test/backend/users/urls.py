from django.contrib import admin
from django.urls import path, include
from users.views import login_view, register_view, HomePage

urlpatterns = [
    path('register/', register_view),
    path('login/', login_view),
    path('home/', HomePage.as_view()),
]
