"""
URL configuration for khumbulekhaya_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from dashboard import views as dashboard_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', dashboard_views.login_view, name='login'),
    path('accounts/register/', dashboard_views.register_view, name='register'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('dashboard/', include('dashboard.urls')),
    path('savings/', include('savings.urls')),
    path('travel/', include('travel.urls')),
    path('invest/', include('invest.urls')),
    path('business/', include('business.urls')),
    path('ai-assistant/', include('ai_assistant.urls')),
    path('', dashboard_views.landing_page, name='landing'),  # Landing page as homepage
]