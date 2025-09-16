from django.urls import path
from . import views

urlpatterns = [
    path('', views.travel_main_view, name='travel_main'),
]