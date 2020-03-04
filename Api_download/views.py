from django.shortcuts import render
from  Api_upload.models import File
# Create your views here.
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from django.http import StreamingHttpResponse

from rest_framework.request import Request
from django.http import QueryDict
def get_parameter_dic(request, *args, **kwargs):
    if isinstance(request, Request) == False:
        return {}

    query_params = request.query_params
    if isinstance(query_params, QueryDict):
        query_params = query_params.dict()
    result_data = request.data
    if isinstance(result_data, QueryDict):
        result_data = result_data.dict()

    if query_params != {}:
        return query_params
    else:
        return result_data

class DonwloadView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, format=None, *args, **kwargs,):

        def file_iterator(fn, chunk_size=512):
            while True:
                c = fn.read(chunk_size)
                if c:
                    yield c
                else:
                    break

        #fn = open('test.zip', 'rb')
        #response = StreamingHttpResponse(file_iterator(fn))
        #file = open('f1.file', 'rb')

        params = get_parameter_dic(request)
        f1=File.objects.get(id=params.get("a"))
        response = StreamingHttpResponse(f1.file)
        name=f1.file.name
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = "attachment;"+"filename="+name

        return response
