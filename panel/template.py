from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import gettext
from base.authentication import authentication_required, permission_required, isAuthenticated

@authentication_required
async def templates(request):
  return render(request, 'template/templates.html', {'title': gettext("templates.title"),
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/template/templates.css']})

@authentication_required
@permission_required(permission = "template.create")
async def templateCreate(request):
  return await template(request, "")

@authentication_required
@permission_required(permission = "template.create")
async def template(request, id):
  return render(request, 'template/template.html', {'title': gettext("template.title"),
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/template/template.css'],
    'template': id})