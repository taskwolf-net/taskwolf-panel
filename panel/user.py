from django.shortcuts import render
from django.http import HttpResponse
from base.authentication import authentication_required, isAuthenticated

@authentication_required
async def users(request):
  return render(request, 'user/users.html', {'title': 'Taskwolf - Users',
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/user/users.css']})

@authentication_required
async def userGeneral(request, id):
  return render(request, 'user/user-general.html', {'title': 'Taskwolf - User',
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/user/user-general.css'],
    'user': id})

@authentication_required
async def userBundle(request, id):
  return render(request, 'user/user-bundle.html', {'title': 'Taskwolf - User',
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/user/user-bundle.css'],
     'user': id})

@authentication_required
async def userBundleChange(request, id):
  return render(request, 'user/user-bundle-change.html', {'title': 'Taskwolf - User',
   'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/user/user-bundle-change.css'],
    'user': id})

@authentication_required
async def userPayment(request, id):
  return render(request, 'user/user-payment.html', {'title': 'Taskwolf - User',
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/user/user-payment.css'],
    'user': id})

@authentication_required
async def userOffer(request, id):
  return render(request, 'user/user-offer.html', {'title': 'Taskwolf - User',
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/user/user-offer.css'],
     'user': id})

@authentication_required
async def userTermination(request, id):
  return render(request, 'user/user-termination.html', {'title': 'Taskwolf - User',
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/user/user-termination.css'],
     'user': id})