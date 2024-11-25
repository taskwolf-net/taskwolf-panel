from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import gettext
from base.authentication import authentication_required, permission_required, isAuthenticated

@authentication_required
@permission_required(permission = "user.search")
async def users(request):
  return render(request, 'user/users.html', {'title': gettext("users.title"),
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/user/users.css']})

@authentication_required
@permission_required(permission = "user.find")
async def userGeneral(request, id):
  return render(request, 'user/user-general.html', {'title': gettext("user.general.title"),
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/entity/entity-tab.css', 'css/panel/user/user-general.css'],
    'user': id, 'entity': id, "type": "user"})

@authentication_required
@permission_required(permission = "mails.find")
async def userMail(request, id):
  return render(request, 'user/user-mail.html', {'title': gettext("user.mail.title"),
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/entity/entity-tab.css', 'css/panel/user/user-mail.css'],
    'user': id, 'entity': id, "type": "user"})

@authentication_required
@permission_required(permission = "sessions.find")
async def userSession(request, id):
  return render(request, 'user/user-session.html', {'title': gettext("user.session.title"),
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/entity/entity-tab.css', 'css/panel/user/user-session.css'],
    'user': id, 'entity': id, "type": "user"})

@authentication_required
@permission_required(permission = "entity.bundle.find")
async def userBundle(request, id):
  return render(request, 'entity/entity-bundle.html', {'title': gettext("user.bundle.title"),
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/entity/entity-tab.css', 'css/panel/entity/entity-bundle.css'],
     'entity': id, "type": "user"})

@authentication_required
@permission_required(permission = "entity.bundle.change")
async def userBundleChange(request, id):
  return render(request, 'entity/entity-bundle-change.html', {'title': gettext("user.bundle.change.title"),
   'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/entity/entity-bundle-change.css'],
    'entity': id, "type": "user"})

@authentication_required
@permission_required(permission = "entity.payments.find")
async def userPayment(request, id):
  return render(request, 'entity/entity-payment.html', {'title': gettext("user.payment.title"),
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/entity/entity-tab.css', 'css/panel/entity/entity-payment.css'],
    'entity': id, "type": "user"})

@authentication_required
@permission_required(permission = "offers.find")
async def userOffers(request, id):
  return render(request, 'entity/entity-offers.html', {'title': gettext("user.offers.title"),
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/entity/entity-tab.css', 'css/panel/entity/entity-offers.css'],
     'entity': id, "type": "user"})

@authentication_required
@permission_required(permission = "entity.termination.status")
async def userTermination(request, id):
  return render(request, 'entity/entity-termination.html', {'title': gettext("user.termination.title"),
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/entity/entity-tab.css', 'css/panel/entity/entity-termination.css'],
     'entity': id, "type": "user"})