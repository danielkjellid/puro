from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('logg-inn/', auth_views.LoginView.as_view(template_name = 'registration/login.html'), name = 'login'),
]

urlpatterns += [
    path('konto/', include('users.frontend_urls')),
    path('backend/users/', include('users.backend_urls')),
]

urlpatterns += [
    path('hijack/', include('hijack.urls'), name='hijack'),
]