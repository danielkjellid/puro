from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include

from . import views as users_views

urlpatterns = [
    path('', users_views.users.as_view(), name='users'),
    path('add/', users_views.addUser, name='add-user'),
    path('export/', users_views.exportUsers, name='users-export'),
    path('<int:pk>/', users_views.user, name='user'),
    path('<int:pk>/edit/', users_views.editUser, name='edit-user'),
    path('<int:pk>/edit/toggle-active', users_views.toggleUser, name='toggle-user'),
    path('<int:pk>/export/', users_views.exportUser, name='export-user'),
    path('<int:pk>/notes/', users_views.userNotes, name='user-notes' ),
    path('<int:pk>/notes/add/', users_views.addNote, name='add-note'),
    path('<int:pk>/changelog/', users_views.userChangelog, name='user-changelog' ),
    path('crm/notes/<int:pk>/delete/', users_views.deleteNote, name='delete-note'),
    path('crm/notes/<int:pk>/edit/', users_views.editNote, name='edit-note'),

    path('test/', users_views.base, name='base'),
]