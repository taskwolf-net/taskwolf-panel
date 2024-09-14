from django.shortcuts import render
from django.http import HttpResponse
from base.authentication import authentication_required, isAuthenticated

@authentication_required
async def sales(request):
  return render(request, 'sale/sales.html', {'title': 'Dulno - Sales',
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/sale/sales.css']})

@authentication_required
async def sale(request, id):
  return render(request, 'sale/sale.html', {'title': 'Dulno - Sale',
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/sale/sale.css'],
    'sale': id})