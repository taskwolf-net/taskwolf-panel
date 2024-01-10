from django.urls import path, include
from . import panel

urlpatterns = [
  path('dashboard/', panel.dashboard)
]