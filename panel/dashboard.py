from django.shortcuts import render
from django.http import HttpResponse
from base.authentication import authentication_required, isAuthenticated

@authentication_required
async def dashboard(request):
  return render(request, 'dashboard/dashboard.html', {'title': 'Taskwolf - Dashboard',
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/dashboard/dashboard.css']})