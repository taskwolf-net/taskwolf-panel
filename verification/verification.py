from django.shortcuts import render
from django.http import HttpResponse

def login(request):
  return render(request, 'login.html', {'title': 'Taskwolf - Login',
    'css': ['css/base/home-header.css', 'css/verification/login.css']})