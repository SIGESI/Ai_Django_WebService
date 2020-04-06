from django.shortcuts import render
from  Api_upload.models import File
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from django.http import JsonResponse
from  reusefunction import get_parameter_dic,file_iterator

import requests
import base64
from googletrans import Translator

# Create your views here.
class BaiduimageView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, format=None, *args, **kwargs, ):
        params = get_parameter_dic(request)  # get param from request
        dbquerey = File.objects.get(remark=params.get("remark"))  # get file from database
        #f = open('tiger.jpg', 'rb')
        dbfile=dbquerey.file
        img = base64.b64encode(dbfile.read())
        host = 'https://aip.baidubce.com/rest/2.0/image-classify/v2/advanced_general'
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        access_token = '24.360c74017f8ebddeebb228841fa6e186.2592000.1588725752.282335-18692896'
        host = host + '?access_token=' + access_token

        data = {}
        data['access_token'] = access_token
        data['image'] = img
        # print(img)
        res = requests.post(url=host, headers=headers, data=data)
        req = res.json()

        translator = Translator()
        for i in range(5):
            req['result'][i]['root']=translator.translate(req['result'][i]['root']).text
            req['result'][i]['keyword']=translator.translate(req['result'][i]['keyword']).text

        return JsonResponse(req,safe=False)