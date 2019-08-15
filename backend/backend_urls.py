from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include

from . import views as backend_views

urlpatterns = [
    path('users/', backend_views.users.as_view(), name="users"),
    path('users/<int:pk>/', backend_views.userDetail, name="user-detail"),
    path('users/<int:pk>/edit/', backend_views.userDetailEdit, name="user-detail-edit"),
]