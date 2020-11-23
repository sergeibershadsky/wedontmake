from django.contrib.auth.views import LogoutView
from django.shortcuts import redirect
from django.urls import path, include

from start.views import login, profile

urlpatterns = [
    path('oauth/', include('social_django.urls', namespace='social')),
    path('', lambda request: redirect('accounts/profile'), name='home'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/login/', login, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
