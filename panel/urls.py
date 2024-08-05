from django.urls import path, include
from . import dashboard, ticket, question, sale, administration

urlpatterns = [
  path('dashboard/', dashboard.dashboard),
  path('tickets/', ticket.tickets),
  path('ticket/<str:id>/', ticket.ticket),
  path('questions/', question.questions),
  path('question/<str:id>/', question.question),
  path('sales/', sale.sales),
  path('sale/<str:id>/', sale.sale),
  path('administration/', administration.administration),
  path('group/<str:name>/', administration.group),
  path('member/<str:id>/', administration.member),
]