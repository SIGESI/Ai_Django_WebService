from django.shortcuts import render

# Create your views here.
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from django.http import StreamingHttpResponse

class DonwloadView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, format=None):

        def file_iterator(fn, chunk_size=512):
            while True:
                c = fn.read(chunk_size)
                if c:
                    yield c
                else:
                    break

        fn = open('test.zip', 'rb')
#        file = open('crm/models.py', 'rb')
        response = StreamingHttpResponse(file_iterator(fn))
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename="test.zip"'

        return response
