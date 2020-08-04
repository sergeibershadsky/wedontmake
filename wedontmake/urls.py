from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include

from start.views import login, profile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('oauth/', include('social_django.urls', namespace='social')),
    path('', lambda request: redirect('accounts/profile')),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/login/', login, name='login')
]
