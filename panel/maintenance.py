from django.shortcuts import render
from django.http import HttpResponse
from base.authentication import authentication_required, isAuthenticated

@authentication_required
async def maintenance(request):
  return render(request, 'maintenance/maintenance.html', {'title': 'Dulno - Maintenance',
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/maintenance/maintenance.css']})

@authentication_required
async def maintenanceCreate(request):
  return render(request, 'maintenance/maintenance-create.html', {'title': 'Dulno - Maintenance - Create',
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/maintenance/maintenance-create.css'],
    'sale': id})