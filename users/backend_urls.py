from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include

from . import views as users_views

urlpatterns = [
    path('', users_views.users.as_view(), name="users"),
    path('export/', users_views.usersExport, name="users-export"),
    path('<int:pk>/', users_views.userDetail, name="user-detail"),
    path('<int:pk>/edit/', users_views.userDetailEdit, name="user-detail-edit"),
    path('<int:pk>/edit/toggle-active', users_views.userDetailEditToggleActive, name="user-detail-edit-toggle"),
    path('<int:pk>/export/', users_views.userDetailExport, name = "user-detail-export"),
]