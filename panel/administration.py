from functools import wraps
from functools import partial
import asyncio
import requests
import json
import jwt
from django.utils import translation
from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import gettext
from base.authentication import authentication_required, isAuthenticated, applyWhitelistKey
from . import dashboard

def administrator_required(function):
  @wraps(function)
  async def authentication(request, *args, **kwargs):
    hasPermission = await hasAdministrationPermission(request)
    if (hasPermission):
      return await function(request, *args, **kwargs)
    return await dashboard.dashboard(request)
  return authentication

async def hasAdministrationPermission(request):
  token = request.COOKIES.get('panel-token')
  if (token is None):
    return False
  headers = {"Authorization": "Bearer " + token}
  applyWhitelistKey(request, headers)
  response = await asyncio.get_event_loop().run_in_executor(None,
    partial(requests.post, "http://10.96.0.9/v1/member/has/permission/",
      headers = headers, json = {"permission": "administrator"}))
  text = response.text
  jsonText = json.loads(text)
  hasPermission = jsonText["hasPermission"]
  return hasPermission

@authentication_required
@administrator_required
async def administration(request):
  return render(request, 'administration/administration.html', {'title': gettext("panel.administration.title"),
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/administration/administration.css']})

@authentication_required
@administrator_required
async def group(request, name):
  return render(request, 'administration/group.html', {'title': gettext("panel.group.title"),
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/administration/group.css'],
    'group': name})

@authentication_required
@administrator_required
async def member(request, id):
  return render(request, 'administration/member.html', {'title': gettext("panel.member.title"),
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/administration/member.css'],
    'member': id})