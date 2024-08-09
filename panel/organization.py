from django.shortcuts import render
from django.http import HttpResponse
from base.authentication import authentication_required, isAuthenticated

@authentication_required
async def organizationGeneral(request, id):
  return render(request, 'organization/organization-general.html', {'title': 'Taskwolf - Organization',
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/organization/organization-general.css'],
    'organization': id})

@authentication_required
async def organizationBundle(request, id):
  return render(request, 'entity/entity-bundle.html', {'title': 'Taskwolf - Organization',
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/entity/entity-bundle.css'],
     'entity': id, "type": "organization"})

@authentication_required
async def organizationBundleChange(request, id):
  return render(request, 'entity/entity-bundle-change.html', {'title': 'Taskwolf - Organization',
   'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/entity/entity-bundle-change.css'],
    'entity': id, "type": "organization"})

@authentication_required
async def organizationPayment(request, id):
  return render(request, 'entity/entity-payment.html', {'title': 'Taskwolf - Organization',
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/entity/entity-payment.css'],
    'entity': id, "type": "organization"})

@authentication_required
async def organizationOffers(request, id):
  return render(request, 'entity/entity-offers.html', {'title': 'Taskwolf - Organization',
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/entity/entity-offers.css'],
     'entity': id, "type": "organization"})

@authentication_required
async def organizationTermination(request, id):
  return render(request, 'entity/entity-termination.html', {'title': 'Taskwolf - Organization',
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/entity/entity-termination.css'],
     'entity': id, "type": "organization"})