from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import gettext
from base.authentication import authentication_required, permission_required, isAuthenticated

@permission_required(permission = "sales.find")
@authentication_required
async def sales(request):
  return render(request, 'sale/sales.html', {'title': gettext("sales.page.title"),
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/sale/sales.css']})

@permission_required(permission = "sale.find")
@authentication_required
async def sale(request, id):
  return render(request, 'sale/sale.html', {'title': gettext("sale.title"),
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/sale/sale.css'],
    'sale': id})