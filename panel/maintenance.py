from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import gettext
from base.authentication import authentication_required, permission_required, isAuthenticated

@permission_required(permission = "maintenance.find")
@authentication_required
async def maintenance(request):
  return render(request, 'maintenance/maintenance.html', {'title': gettext("maintenance.title"),
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/maintenance/maintenance.css']})

@permission_required(permission = "maintenance.create")
@authentication_required
async def maintenanceCreate(request):
  return render(request, 'maintenance/maintenance-create.html', {'title': gettext("maintenance.create.title"),
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/maintenance/maintenance-create.css'],
    'sale': id})