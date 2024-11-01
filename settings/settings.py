from django.shortcuts import render
from django.http import HttpResponse
from base.authentication import authentication_required, isAuthenticated
from django.utils.translation import gettext

@authentication_required
async def profileSettings(request):
  return render(request, 'settings-profile.html', {'title': gettext('settings.profile.title'),
    'css': ['css/base/settings-header.css', 'css/base/settings-sidebar.css', 'css/base/settings.css', 'css/settings/settings-profile.css']})

@authentication_required
async def accountSettings(request):
  return render(request, 'settings-account.html', {'title': gettext('settings.account.title'),
    'css': ['css/base/settings-header.css', 'css/base/settings-sidebar.css', 'css/base/settings.css', 'css/settings/settings-account.css']})

@authentication_required
async def languageSettings(request):
  return render(request, 'settings-language.html', {'title': gettext('settings.language.title'),
    'css': ['css/base/settings-header.css', 'css/base/settings-sidebar.css', 'css/base/settings.css', 'css/settings/settings-language.css']})

@authentication_required
async def themeSettings(request):
  return render(request, 'settings-theme.html', {'title': gettext('settings.theme.title'),
    'css': ['css/base/settings-header.css', 'css/base/settings-sidebar.css', 'css/base/settings.css', 'css/settings/settings-theme.css']})

@authentication_required
async def twoFactorAuthenticationSettings(request):
  return render(request, 'settings-2fa.html', {'title': gettext('settings.2fa.title'),
    'css': ['css/base/settings-header.css', 'css/base/settings-sidebar.css', 'css/base/2fa.css', 'css/base/settings.css', 'css/settings/settings-2fa.css']})