from django.shortcuts import render
from django.http import HttpResponse
from base.authentication import authentication_required, isAuthenticated

@authentication_required
async def users(request):
  return render(request, 'user/users.html', {'title': 'Taskwolf - Users',
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/user/users.css']})

@authentication_required
async def user(request, id):
  return render(request, 'user/user.html', {'title': 'Taskwolf - User',
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/user/user.css'], 'user': id})