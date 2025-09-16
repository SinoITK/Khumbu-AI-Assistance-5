from django.urls import path
from . import views

urlpatterns = [
    path('', views.business_main_view, name='business_main'),
]