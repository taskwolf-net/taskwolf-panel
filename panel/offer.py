from django.shortcuts import render
from django.http import HttpResponse
from base.authentication import authentication_required, isAuthenticated

@authentication_required
async def offer(request, id):
  return render(request, 'offer/offer.html', {'title': 'Taskwolf - Offer',
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/offer/offer.css'],
     'offer': id})

@authentication_required
async def createOffer(request, id):
  return render(request, 'offer/offer-create.html', {'title': 'Taskwolf - Offer',
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/offer/offer-create.css'],
      'target': id})