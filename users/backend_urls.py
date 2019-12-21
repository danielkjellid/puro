from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include

from . import views as users_views

urlpatterns = [
    #updated
    path('', users_views.users.as_view(), name="users"),
    path('<int:pk>/notes/', users_views.userNotes, name="user-notes" ),
    path('<int:pk>/', users_views.user, name="user"),
    
    path('crm/notes/edit/<int:pk>', users_views.changeNote, name="change-note"),
    #not updated
    path('export/', users_views.usersExport, name="users-export"),
    path('<int:pk>/', users_views.user, name="user"),
    path('<int:pk>/edit/', users_views.userDetailEdit, name="user-detail-edit"),
    path('<int:pk>/edit/toggle-active', users_views.userDetailEditToggleActive, name="user-detail-edit-toggle"),
    path('<int:pk>/export/', users_views.userDetailExport, name = "user-detail-export"),
]