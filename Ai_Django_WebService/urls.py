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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from App_helloWorld.views import hello,helloAction
#from Api_upload.views import FileView
#from Api_download.views import DonwloadView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello),
    path('helloAction/', helloAction),

    path('api/', include('Api_upload.url')),   #path('upload/', FileView.as_view(), name='file-upload'),
    path('api/', include('Api_download.url')), #path('download/', DonwloadView.as_view(), name='file-download'),
    path('api/', include('Api_baidu_image.url')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)