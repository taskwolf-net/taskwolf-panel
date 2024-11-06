from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import gettext
from base.authentication import authentication_required, isAuthenticated

@authentication_required
async def clusterResource(request):
  return render(request, 'cluster/cluster-resource.html', {'title': gettext("cluster.resource.title"),
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/cluster/cluster-tab.css',
      'css/panel/cluster/cluster-resource.css']})

@authentication_required
async def clusterServer(request):
  return render(request, 'cluster/cluster-server.html', {'title': gettext("cluster.server.title"),
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/cluster/cluster-tab.css',
      'css/panel/cluster/cluster-server.css']})