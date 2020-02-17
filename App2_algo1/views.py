from django.shortcuts import render
import os
from json import load
from urllib import request as req
# Create your views here.
def algo1(request):
    #return HttpResponse("myapp2")

    ipindex = load(req.urlopen('http://jsonip.com'))['ip']
    ipindex = "http://" + str(ipindex) + ":8005/algo1/"
    category="cat"
    dict={'data': category, 'ipindex': ipindex}
    return render(request, "algo1.html",dict)

def algo1_upload(request):

    File = request.FILES.get("myfile", None)
    image_path = "./App2_algo1/images/"+"%s"%File.name #+ "%s" % File.name

    # open file to write
    with open(image_path, 'wb+') as f:
        # Write to file in chunks
        for chunk in File.chunks():
            f.write(chunk)
    c="humen"
    ipindex = load(req.urlopen('http://jsonip.com'))['ip']
    ipindex = "http://" + str(ipindex) + ":8005/algo1/"
    dict = {'data': c, 'ipindex': ipindex}
    return render(request, "algo1.html",dict)#,locals())
