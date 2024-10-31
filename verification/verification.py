from functools import wraps
from functools import partial
from django.shortcuts import render
from django.http import HttpResponse
from base.authentication import isAuthenticated
from panel.dashboard import dashboard
from django.utils import translation
from django.utils.translation import gettext

def verification_page(function):
  @wraps(function)
  async def verification_page(request, *args, **kwargs):
    translation.activate("en")
    return await function(request, *args, **kwargs)
  return verification_page

@verification_page
async def login(request):
  authenticated = await isAuthenticated(request)
  if (authenticated):
    return await dashboard(request)
  return render(request, 'login.html', {'title': 'Panel - Dulno',
    'css': ['css/verification/login.css']})

@verification_page
async def confirm(request, member, token):
  return render(request, 'confirm.html', {'title': "Dulno - Confirmation",
    'css': ['css/verification/confirm.css'],
    'member': member, 'token': token})