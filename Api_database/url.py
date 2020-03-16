from django.urls import path,include
from .views import Getfilename

urlpatterns = [
    path('getfilename/', Getfilename.as_view(), name='getfilename'),
]