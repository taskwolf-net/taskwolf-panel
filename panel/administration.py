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
from base.authentication import authentication_required, permission_required, isAuthenticated, applyWhitelistKey
from . import dashboard

@permission_required(permission = "groups.find")
@authentication_required
async def administration(request):
  return render(request, 'administration/administration.html', {'title': gettext("panel.administration.title"),
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/administration/administration.css']})

@permission_required(permission = "groups.find")
@authentication_required
async def group(request, name):
  return render(request, 'administration/group.html', {'title': gettext("panel.group.title"),
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/administration/group.css'],
    'group': name})

@permission_required(permission = "members.find")
@authentication_required
async def member(request, id):
  return render(request, 'administration/member.html', {'title': gettext("panel.member.title"),
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/administration/member.css'],
    'member': id})