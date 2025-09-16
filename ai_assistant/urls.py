from django.urls import path
from . import views

urlpatterns = [
    path('', views.ai_assistant_view, name='ai_assistant'),
]