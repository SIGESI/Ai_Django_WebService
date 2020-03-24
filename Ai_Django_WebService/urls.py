"""Ai_Django_WebService URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path

from App1_login_home.views import Login_home_view

from App2_image_rec.views import Img_rec_view

urlpatterns = [
    path('admin/', admin.site.urls),
    # app1 login
    path('login/', Login_home_view.login),
    path('login_action/', Login_home_view.login_action),
    path('logout/', Login_home_view.logout),
    # app1 home(index)
    path('index/', Login_home_view.index),
    path('index_action/', Login_home_view.index_action),
    path('img_rec/', Img_rec_view.img_rec),
    path('img_rec_action/', Img_rec_view.img_rec_action),
]
