"""Defines URL patterns for accounts."""

from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    # Include default auth URLs for login, logout, password management, etc.
    path('', include('django.contrib.auth.urls')),

    # Custom registration page.
    path('register/', views.register, name='register'),

    # Optionally, you can redefine login and logout views if needed:
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
