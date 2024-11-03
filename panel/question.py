from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import gettext
from base.authentication import authentication_required, isAuthenticated

@authentication_required
async def questions(request):
  return render(request, 'question/questions.html', {'title': gettext("questions.page.title"),
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/question/questions.css']})

@authentication_required
async def question(request, id):
  return render(request, 'question/question.html', {'title': gettext("question.title"),
    'css': ['css/base/panel-header.css', 'css/base/panel-sidebar.css', 'css/panel/question/question.css'],
    'question': id})