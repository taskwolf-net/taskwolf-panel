from django.shortcuts import render
from django.http import HttpResponse
from base.authentication import authentication_required, isAuthenticated

@authentication_required
async def organization(request, id):
  return render(request, 'user/user.html', {'title': 'Taskwolf - Organization',
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/organization/organization.css'],
    'organization': id})