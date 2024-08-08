from django.urls import path, include
from . import dashboard, ticket, question, sale, user, organization, offer, administration

urlpatterns = [
  path('dashboard/', dashboard.dashboard),
  path('tickets/', ticket.tickets),
  path('ticket/<str:id>/', ticket.ticket),
  path('questions/', question.questions),
  path('question/<str:id>/', question.question),
  path('sales/', sale.sales),
  path('sale/<str:id>/', sale.sale),
  path('users/', user.users),
  path('user/<str:id>/general/', user.userGeneral),
  path('user/<str:id>/bundle/', user.userBundle),
  path('user/<str:id>/bundle/change/', user.userBundleChange),
  path('user/<str:id>/payment/', user.userPayment),
  path('user/<str:id>/offers/', user.userOffers),
  path('user/<str:id>/offer/create/', offer.createUserOffer),
  path('user/<str:id>/termination/', user.userTermination),
  path('offer/<str:id>/', offer.offer),
  path('organization/<str:id>/', organization.organization),
  path('administration/', administration.administration),
  path('group/<str:name>/', administration.group),
  path('member/<str:id>/', administration.member),
]