from django.urls import path, include
from . import panel

urlpatterns = [
  path('dashboard/', panel.dashboard),
  path('tickets/', panel.tickets),
  path('ticket/<str:id>/', panel.ticket),
  path('emails/', panel.emails),
  path('email/<str:id>/', panel.email),
]