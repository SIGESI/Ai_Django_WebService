from django.shortcuts import render
from  Api_upload.models import File
# Create your views here.
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from django.http import StreamingHttpResponse

from  reusefunction import get_parameter_dic,file_iterator

class DonwloadView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, format=None, *args, **kwargs,):

        #for big file
        #fn = open('test.zip', 'rb')
        #response = StreamingHttpResponse(file_iterator(fn))
        #file = open('f1.file', 'rb')

        params = get_parameter_dic(request)# get param from request
        file=File.objects.get(id=params.get("filename")) # get file from database
        response = StreamingHttpResponse(file.file)
        name=file.file.name
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = "attachment;"+"filename="+name

        return response
