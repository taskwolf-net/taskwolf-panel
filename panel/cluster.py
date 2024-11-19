from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import gettext
from base.authentication import authentication_required, permission_required, isAuthenticated

@permission_required(permission = "cluster.resources")
@authentication_required
async def clusterResources(request):
  return render(request, 'cluster/cluster-resources.html', {'title': gettext("cluster.resources.title"),
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/cluster/cluster-tab.css',
      'css/panel/cluster/cluster-resources.css']})

@permission_required(permission = "cluster.resources")
@authentication_required
async def clusterServices(request):
  return render(request, 'cluster/cluster-services.html', {'title': gettext("cluster.services.title"),
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/cluster/cluster-tab.css',
      'css/panel/cluster/cluster-services.css']})

@permission_required(permission = "cluster.servers")
@authentication_required
async def clusterServers(request):
  return render(request, 'cluster/cluster-servers.html', {'title': gettext("cluster.servers.title"),
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/cluster/cluster-tab.css',
      'css/panel/cluster/cluster-servers.css']})

@permission_required(permission = "cluster.server")
@authentication_required
async def clusterServer(request, id):
  return render(request, 'cluster/cluster-server.html', {'title': gettext("cluster.server.title"),
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css',
      'css/panel/cluster/cluster-server.css'], 'id': id})

@permission_required(permission = "cluster.units")
@authentication_required
async def clusterUnits(request):
  return render(request, 'cluster/cluster-units.html', {'title': gettext("cluster.units.title"),
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/cluster/cluster-tab.css',
      'css/panel/cluster/cluster-units.css']})

@permission_required(permission = "cluster.unit")
@authentication_required
async def clusterUnit(request, type, name):
  return render(request, 'cluster/cluster-unit.html', {'title': gettext("cluster.unit.title"),
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css',
      'css/panel/cluster/cluster-unit.css'], 'type': type, 'name': name})

@permission_required(permission = "cluster.pod")
@authentication_required
async def clusterUnitPod(request, unitType, unitName, podName):
  return render(request, 'cluster/cluster-unit-pod.html', {'title': gettext("cluster.unit.pod.title"),
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css',
      'css/panel/cluster/cluster-unit-pod.css'], 'unitType': unitType,
    'unitName': unitName, 'podName': podName})

@permission_required(permission = "cluster.errors")
@authentication_required
async def clusterErrors(request):
  return render(request, 'cluster/cluster-errors.html', {'title': gettext("cluster.errors.title"),
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/cluster/cluster-tab.css',
      'css/panel/cluster/cluster-errors.css']})