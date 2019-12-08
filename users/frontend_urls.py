from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include

from . import views as users_views

urlpatterns = [
    #path('', users_views.account.as_view(), name="account"),
]