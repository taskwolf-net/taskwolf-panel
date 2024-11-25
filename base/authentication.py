from functools import wraps
from functools import partial
import asyncio
import requests
import json
import jwt
import datetime
from django.utils import translation
from django.conf import settings
from django.shortcuts import redirect

def authentication_required(function):
  @wraps(function)
  async def authentication(request, *args, **kwargs):
    authenticationResponse = await isAuthenticated(request)
    if (authenticationResponse["success"]):
      if ("data" in authenticationResponse):
        request.COOKIES["panel-token"] = authenticationResponse["data"]["panel-token"]
        request.COOKIES["panel-refresh-token"] = authenticationResponse["data"]["refreshToken"]
      language = await applyLanguage(request)
      response = await function(request, *args, **kwargs)
      if ("data" in authenticationResponse):
        setCookie(response, "panel-token", authenticationResponse["data"]["panel-token"], 30)
        setCookie(response, "panel-refresh-token", authenticationResponse["data"]["refreshToken"], 30)
      return response
    response = redirect("/")
    response.delete_cookie("panel-token", domain=".dulno.com")
    response.delete_cookie("panel-refresh-token", domain=".dulno.com")
    return response
  return authentication

async def isAuthenticated(request):
  token = request.COOKIES.get("panel-token")
  if (token is None):
    return await refreshAuthentication(request)
  headers = {}
  applyWhitelistKey(request, headers)
  response = await asyncio.get_event_loop().run_in_executor(None,
    partial(requests.post, "http://10.96.0.9/v1/verification/isValid/",
      json = {"token": token}, headers = headers))
  if (response.status_code == 417):
    return await refreshAuthentication(request)
  text = response.text
  jsonText = json.loads(text)
  isValid = jsonText["isValid"]
  if (isValid == "true"):
    return {"success": True}
  return {"success": False}

async def refreshAuthentication(request):
  refreshToken = request.COOKIES.get("panel-refresh-token")
  if (refreshToken is None):
    return {"success": False}
  headers = {}
  applyWhitelistKey(request, headers)
  response = await asyncio.get_event_loop().run_in_executor(None,
    partial(requests.post, "http://10.96.0.9/v1/verification/refresh/",
      json = {"refreshToken": refreshToken}, headers = headers))
  text = response.text
  jsonText = json.loads(text)
  success = jsonText["success"]
  if (success == "true"):
    request.dulnoToken = jsonText["panelApiKey"]
    request.dulnoRefreshToken = jsonText["refreshToken"]
    return {"success": True, "data": {"panel-token": jsonText["panelApiKey"],
      "refreshToken": jsonText["refreshToken"]}}
  return {"success": False}

async def applyLanguage(request):
  token = request.COOKIES.get('panel-token')
  if (token is None):
    translation.activate("en")
    return False
  headers = {"Authorization": "Bearer " + token}
  applyWhitelistKey(request, headers)
  response = await asyncio.get_event_loop().run_in_executor(None,
    partial(requests.get, "http://10.96.0.9/v1/settings/language/",
    headers = headers))
  text = response.text
  jsonText = json.loads(text)
  translation.activate(jsonText["language"])

def applyWhitelistKey(request, headers):
  if (not settings.WHITELIST):
    return
  whitelistKey = request.COOKIES.get('dulno-whitelist-key')
  if (whitelistKey != None):
    headers["WHITELIST-KEY"] = whitelistKey

def permission_required(permission):
  def wrapper(function):
    @wraps(function)
    async def authentication(request, *args, **kwargs):
      hasPermission = await checkPermission(request, permission)
      if (hasPermission):
        return await function(request, *args, **kwargs)
      return redirect("/")
    return authentication
  return wrapper

async def checkPermission(request, permission):
  token = request.COOKIES.get('panel-token')
  if (token is None):
    return False
  headers = {"Authorization": "Bearer " + token}
  applyWhitelistKey(request, headers)
  response = await asyncio.get_event_loop().run_in_executor(None,
    partial(requests.post, "http://10.96.0.9/v1/member/has/permission/",
      headers = headers, json = {"permission": permission}))
  text = response.text
  jsonText = json.loads(text)
  hasPermission = jsonText["hasPermission"]
  return hasPermission

def setCookie(response, key, value, expirationDays):
  expires = datetime.datetime.strftime(datetime.datetime.utcnow() +
    datetime.timedelta(days=expirationDays), "%a, %d-%b-%Y %H:%M:%S GMT")
  response.set_cookie(key, value, expires=expires, domain=".dulno.com",
    secure=True)