from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import gettext
from base.authentication import authentication_required, permission_required, isAuthenticated

@authentication_required
@permission_required(permission = "cluster.resources")
async def clusterResources(request):
  return render(request, 'cluster/cluster-resources.html', {'title': gettext("cluster.resources.title"),
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/cluster/cluster-tab.css',
      'css/panel/cluster/cluster-resources.css']})

@authentication_required
@permission_required(permission = "cluster.resources")
async def clusterServices(request):
  return render(request, 'cluster/cluster-services.html', {'title': gettext("cluster.services.title"),
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/cluster/cluster-tab.css',
      'css/panel/cluster/cluster-services.css']})

@authentication_required
@permission_required(permission = "cluster.servers")
async def clusterServers(request):
  return render(request, 'cluster/cluster-servers.html', {'title': gettext("cluster.servers.title"),
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/cluster/cluster-tab.css',
      'css/panel/cluster/cluster-servers.css']})

@authentication_required
@permission_required(permission = "cluster.server")
async def clusterServer(request, id):
  return render(request, 'cluster/cluster-server.html', {'title': gettext("cluster.server.title"),
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css',
      'css/panel/cluster/cluster-server.css'], 'id': id})

@authentication_required
@permission_required(permission = "cluster.units")
async def clusterUnits(request):
  return render(request, 'cluster/cluster-units.html', {'title': gettext("cluster.units.title"),
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/cluster/cluster-tab.css',
      'css/panel/cluster/cluster-units.css']})

@authentication_required
@permission_required(permission = "cluster.unit")
async def clusterUnit(request, type, name):
  return render(request, 'cluster/cluster-unit.html', {'title': gettext("cluster.unit.title"),
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css',
      'css/panel/cluster/cluster-unit.css'], 'type': type, 'name': name})

@authentication_required
@permission_required(permission = "cluster.pod")
async def clusterUnitPod(request, unitType, unitName, podName):
  return render(request, 'cluster/cluster-unit-pod.html', {'title': gettext("cluster.unit.pod.title"),
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css',
      'css/panel/cluster/cluster-unit-pod.css'], 'unitType': unitType,
    'unitName': unitName, 'podName': podName})

@authentication_required
@permission_required(permission = "cluster.backups")
async def clusterBackups(request):
  return render(request, 'cluster/cluster-backups.html', {'title': gettext("cluster.backups.title"),
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/cluster/cluster-tab.css',
      'css/panel/cluster/cluster-backups.css']})

@authentication_required
@permission_required(permission = "cluster.errors")
async def clusterErrors(request):
  return render(request, 'cluster/cluster-errors.html', {'title': gettext("cluster.errors.title"),
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/cluster/cluster-tab.css',
      'css/panel/cluster/cluster-errors.css']})