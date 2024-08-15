"""
URL configuration for quizzer project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.shortcuts import render
from django.urls import path

from core.forms import RegisterForm


def index(request):
    return render(request, "index.html")

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            return render(request, "register.html", {"form": form})
    else:
        form = RegisterForm()
    return render(request, "register.html", {"form": form})

def login(request):
    return render(request, "login.html")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index),
    path("register/", register),

    path("login/", login),
]
