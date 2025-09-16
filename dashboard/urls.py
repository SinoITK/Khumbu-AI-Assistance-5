from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),
    path('profile/', views.profile_view, name='profile'),
    path('profile/edit/', views.profile_edit_view, name='profile_edit'),
    path('profile/user/edit/', views.user_profile_edit_view, name='user_profile_edit'),
    path('security/change-password/', views.change_password_view, name='change_password'),
    path('security/login-history/', views.login_history_view, name='login_history'),
    path('security/two-factor/', views.two_factor_setup_view, name='two_factor_setup'),
    path('preferences/update/', views.update_preferences_view, name='update_preferences'),
]