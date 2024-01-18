from django.shortcuts import render
from django.http import HttpResponse
from base.authentication import authentication_required, isAuthenticated

@authentication_required
async def emails(request):
  return render(request, 'email/emails.html', {'title': 'Taskwolf - Emails',
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/email/emails.css']})

@authentication_required
async def email(request, id):
  return render(request, 'email/email.html', {'title': 'Taskwolf - Email',
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/email/email.css'], 'email': id})