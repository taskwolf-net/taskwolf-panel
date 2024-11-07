from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import gettext
from base.authentication import authentication_required, isAuthenticated

@authentication_required
async def clusterResources(request):
  return render(request, 'cluster/cluster-resources.html', {'title': gettext("cluster.resources.title"),
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/cluster/cluster-tab.css',
      'css/panel/cluster/cluster-resources.css']})

@authentication_required
async def clusterServers(request):
  return render(request, 'cluster/cluster-servers.html', {'title': gettext("cluster.servers.title"),
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/cluster/cluster-tab.css',
      'css/panel/cluster/cluster-servers.css']})

@authentication_required
async def clusterUnits(request):
  return render(request, 'cluster/cluster-units.html', {'title': gettext("cluster.units.title"),
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/cluster/cluster-tab.css',
      'css/panel/cluster/cluster-units.css']})

@authentication_required
async def clusterErrors(request):
  return render(request, 'cluster/cluster-errors.html', {'title': gettext("cluster.errors.title"),
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/cluster/cluster-tab.css',
      'css/panel/cluster/cluster-errors.css']})