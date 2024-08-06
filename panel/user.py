from django.shortcuts import render
from django.http import HttpResponse
from base.authentication import authentication_required, isAuthenticated

@authentication_required
async def users(request):
  return render(request, 'user/users.html', {'title': 'Taskwolf - Users',
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/user/users.css']})

@authentication_required
async def userGeneral(request, id):
  return render(request, 'user/user-general.html', {'title': 'Taskwolf - User - General',
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/user/user-general.css'],
    'user': id})

@authentication_required
async def userOrganization(request, id):
  return render(request, 'user/user-organization.html', {'title': 'Taskwolf - User - Organization',
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/user/user-organization.css'],
    'user': id})

@authentication_required
async def userBundle(request, id):
  return render(request, 'user/user-bundle.html', {'title': 'Taskwolf - User - Bundle',
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/user/user-bundle.css'],
     'user': id})

@authentication_required
async def userPayment(request, id):
  return render(request, 'user/user-payment.html', {'title': 'Taskwolf - User - Payment',
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/user/user-payment.css'],
    'user': id})

@authentication_required
async def userTermination(request, id):
  return render(request, 'user/user-termination.html', {'title': 'Taskwolf - User - Termination',
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/user/user-termination.css'],
     'user': id})