from django.urls import path, include
from . import dashboard, ticket, email, administration

urlpatterns = [
  path('dashboard/', dashboard.dashboard),
  path('tickets/', ticket.tickets),
  path('ticket/<str:id>/', ticket.ticket),
  path('emails/', email.emails),
  path('email/<str:id>/', email.email),
  path('administration/', administration.administration),
  path('group/<str:name>/', administration.group),
  path('member/<str:id>/', administration.member),
]