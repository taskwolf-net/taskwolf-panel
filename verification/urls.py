from django.urls import path, include
from . import verification

urlpatterns = [
  path('', verification.login),
]