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
  return render(request, 'entity/entity-bundle.html', {'title': 'Taskwolf - User',
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/entity/entity-bundle.css'],
     'entity': id, "type": "user"})

@authentication_required
async def userBundleChange(request, id):
  return render(request, 'entity/entity-bundle-change.html', {'title': 'Taskwolf - User',
   'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/entity/entity-bundle-change.css'],
    'entity': id, "type": "user"})

@authentication_required
async def userPayment(request, id):
  return render(request, 'entity/entity-payment.html', {'title': 'Taskwolf - User',
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/entity/entity-payment.css'],
    'entity': id, "type": "user"})

@authentication_required
async def userOffers(request, id):
  return render(request, 'entity/entity-offers.html', {'title': 'Taskwolf - User',
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/entity/entity-offers.css'],
     'entity': id, "type": "user"})

@authentication_required
async def userTermination(request, id):
  return render(request, 'entity/entity-termination.html', {'title': 'Taskwolf - User',
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/entity/entity-termination.css'],
     'entity': id, "type": "user"})