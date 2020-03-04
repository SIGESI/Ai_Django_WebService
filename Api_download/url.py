from django.urls import path,include
from .views import DonwloadView

urlpatterns = [
    path('download/', DonwloadView.as_view(), name='file-download'),
]