from django.urls import path
from . import views

urlpatterns = [
    path('', views.investments_main_view, name='investments_main'),
    path('projections/', views.investment_projections_view, name='investment_projections'),
]