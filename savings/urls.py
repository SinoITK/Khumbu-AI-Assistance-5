from django.urls import path
from . import views

urlpatterns = [
    path('integrated-overview/', views.savings_dashboard_view, name='savings_dashboard'),
    path('stokvel-transactions/', views.stokvel_transactions_view, name='stokvel_transactions'),
]