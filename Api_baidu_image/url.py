from django.urls import path,include
from .views import BaiduimageView

urlpatterns = [
    path('image_recognition/', BaiduimageView.as_view(), name='image_recognition'),
]