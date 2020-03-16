from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from  Api_upload.models import File
from  reusefunction import get_parameter_dic
from django.http import JsonResponse

# Create your views here.
class Getfilename(APIView):
    permission_classes = (AllowAny,)
    def get(self, request, format=None, *args, **kwargs, ):
        params = get_parameter_dic(request)
        dbquerey = File.objects.get(remark=params.get("remark"))
        dbfile = dbquerey.file
        filename = dbfile.name
        filenameDic={'filename':filename}
        return JsonResponse(filenameDic,safe=False)