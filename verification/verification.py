from django.shortcuts import render
from django.http import HttpResponse
from base.authentication import isAuthenticated
from panel.dashboard import dashboard

async def login(request):
  authenticated = await isAuthenticated(request)
  if (authenticated):
    return await dashboard(request)
  return render(request, 'login.html', {'title': 'Taskwolf - Login',
    'css': ['css/verification/login.css']})