from django.shortcuts import render
from django.http import HttpResponse
from base.authentication import authentication_required, isAuthenticated

@authentication_required
async def offer(request, id):
  return render(request, 'offer/offer.html', {'title': 'Taskwolf - Offer',
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/offer/offer.css'],
     'offer': id})

@authentication_required
async def createUserOffer(request, id):
  return await createOffer(request, id, "user")

@authentication_required
async def createOrganizationOffer(request, id):
  return await createOffer(request, id, "organization")

@authentication_required
async def createOffer(request, id, type):
  return render(request, 'offer/offer-create.html', {'title': 'Taskwolf - Offer',
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/offer/offer-create.css'],
      'target': id, "type": type})