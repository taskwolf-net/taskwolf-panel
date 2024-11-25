from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import gettext
from base.authentication import authentication_required, permission_required, isAuthenticated

@authentication_required
@permission_required(permission = "organization.find")
async def organizationGeneral(request, id):
  return render(request, 'organization/organization-general.html', {'title': gettext("organization.general.title"),
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/entity/entity-tab.css', 'css/panel/organization/organization-general.css'],
    'organization': id, 'entity': id, "type": "organization"})

@authentication_required
@permission_required(permission = "entity.bundle.find")
async def organizationBundle(request, id):
  return render(request, 'entity/entity-bundle.html', {'title': gettext("organization.bundle.title"),
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/entity/entity-tab.css', 'css/panel/entity/entity-bundle.css'],
     'entity': id, "type": "organization"})

@authentication_required
@permission_required(permission = "entity.bundle.change")
async def organizationBundleChange(request, id):
  return render(request, 'entity/entity-bundle-change.html', {'title': gettext("organization.bundle.change.title"),
   'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/entity/entity-tab.css', 'css/panel/entity/entity-bundle-change.css'],
    'entity': id, "type": "organization"})

@authentication_required
@permission_required(permission = "entity.payments.find")
async def organizationPayment(request, id):
  return render(request, 'entity/entity-payment.html', {'title': gettext("organization.payment.title"),
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/entity/entity-tab.css', 'css/panel/entity/entity-payment.css'],
    'entity': id, "type": "organization"})

@authentication_required
@permission_required(permission = "offers.find")
async def organizationOffers(request, id):
  return render(request, 'entity/entity-offers.html', {'title': gettext("organization.offers.title"),
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/entity/entity-tab.css', 'css/panel/entity/entity-offers.css'],
     'entity': id, "type": "organization"})

@authentication_required
@permission_required(permission = "entity.termination.status")
async def organizationTermination(request, id):
  return render(request, 'entity/entity-termination.html', {'title': gettext("organization.termination.title"),
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/entity/entity-tab.css', 'css/panel/entity/entity-termination.css'],
     'entity': id, "type": "organization"})