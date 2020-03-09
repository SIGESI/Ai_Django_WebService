from django.shortcuts import render
import os
from json import load
from urllib import request as req
import requests
# Create your views here.

# Create your views here.
def img_rec(request):
    #return HttpResponse("myapp2")

    ipindex = load(req.urlopen('http://jsonip.com'))['ip']
    ipindex = "http://" + str(ipindex) + ":8005/index/"
    dict={ 'ipindex': ipindex}
    return render(request, "img_recognition.html", dict)

def img_rec_action(request):

    ipindex = load(req.urlopen('http://jsonip.com'))['ip']
    url = "http://" + str(ipindex) + ":8009/api/upload/"  # production
    #url = "http://localhost:8000/api/upload/"  # local test, Commented out in production

    fileDic = {'file': request.FILES.get("file", None)}
    rmarkDic = {'remark': request.POST.get("remark")}  # post.get -> WSGI request
    requests.post(url, data=rmarkDic, files=fileDic)

    recurl = "http://" + str(ipindex) + ":8009/api/image_recognition/"  # production
    #recurl = "http://localhost:8000/api/image_recognition/"
    rep = requests.get(recurl, data=rmarkDic)

    keyword = []
    root = []
    score = []
    dict = {}
    resjson = rep.json()
    for i in range(5):
        # keyword[i]= resjson['result'][i]['keyword']
        # root[i]= resjson['result'][i]['root']
        # score[i]= resjson['result'][i]['score']
        dict['keyword' + str(i + 1)] = resjson['result'][i]['keyword']
        dict['root' + str(i + 1)] = resjson['result'][i]['root']
        dict['score' + str(i + 1)] = resjson['result'][i]['score']

    return render(request, "img_recognition.html", dict)
