from django.urls import path,include
from .views import FileView

urlpatterns = [
    path('upload/', FileView.as_view(), name='file-upload'),
]