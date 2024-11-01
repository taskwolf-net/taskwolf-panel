from django.urls import path, include
from . import verification

urlpatterns = [
  path('', verification.login),
  path('confirm/<str:member>/<str:token>/', verification.confirm),
  path('password/reset/request/', verification.passwordResetRequest),
  path('password/reset/complete/<str:member>/<str:token>/', verification.passwordResetComplete),
]