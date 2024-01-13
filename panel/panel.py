from django.shortcuts import render
from django.http import HttpResponse
from base.authentication import authentication_required, isAuthenticated

@authentication_required
async def dashboard(request):
  return render(request, 'dashboard/dashboard.html', {'title': 'Taskwolf - Dashboard',
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/dashboard/dashboard.css']})

@authentication_required
async def tickets(request):
  return render(request, 'ticket/tickets.html', {'title': 'Taskwolf - Tickets',
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/ticket/tickets.css']})

@authentication_required
async def ticket(request, id):
  return render(request, 'ticket/ticket.html', {'title': 'Taskwolf - Ticket',
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/ticket/ticket.css'], 'ticket': id})

@authentication_required
async def emails(request):
  return render(request, 'email/emails.html', {'title': 'Taskwolf - Emails',
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/email/emails.css']})

@authentication_required
async def email(request, id):
  return render(request, 'email/email.html', {'title': 'Taskwolf - Email',
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/email/email.css'], 'email': id})