from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import gettext
from base.authentication import authentication_required, permission_required, isAuthenticated

@authentication_required
@permission_required(permission = "tickets.find")
async def tickets(request):
  return render(request, 'ticket/tickets.html', {'title': gettext("tickets.page.title"),
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/ticket/tickets.css']})

@authentication_required
@permission_required(permission = "ticket.find")
async def ticket(request, id):
  return render(request, 'ticket/ticket.html', {'title': gettext("ticket.title"),
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/ticket/ticket.css'], 'ticket': id})