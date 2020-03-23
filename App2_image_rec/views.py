from django.shortcuts import render
import os
from json import load
from urllib import request as req
import requests
import json
from django.contrib.auth.decorators import login_required
import random

@login_required
def img_rec(request):
    ip_parameter=Get_ip_parameter()
    ip_parameter.get_ip_parameter_test()
    ipindex = ip_parameter.ipindex
    dict={ 'ipindex': ipindex,'resultshow':'display: none;', 'resulpath':'/Sharedvolume/static/home/img/team/team-01.jpg'}

    return render(request, "img_recognition.html", dict)
@login_required
def img_rec_action(request):
    ip_parameter=Get_ip_parameter()
    ip_parameter.get_ip_parameter_test()
    if (request.FILES.get("file", None)) is not None:#and (request.POST.get("remark")) is not None:
        remark=''
        if (request.POST.get("remark")) is not None:
            remark = request.POST.get("remark")
        randomkey=''.join(random.sample(['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a'], 6))
        sessionkey = request.session.session_key
        remark = remark + sessionkey+randomkey
        url=ip_parameter.url
        fileDic = {'file': request.FILES.get("file", None)}
        rmarkDic = {'remark': remark}  # post.get -> WSGI request
        requests.post(url, data=rmarkDic, files=fileDic)



        filenameurl = ip_parameter.filenameurl
        fnrep = requests.get(filenameurl, data=rmarkDic)
        fnrepjson = fnrep.json()

        recurl = ip_parameter.recurl
        rep = requests.get(recurl, data=rmarkDic)
        dict = {}
        resjson = rep.json()

        for i in range(5):
            dict['keyword' + str(i + 1)] = resjson['result'][i]['keyword']
            dict['root' + str(i + 1)] = resjson['result'][i]['root']
            dict['score' + str(i + 1)] = resjson['result'][i]['score']

        ipindex = ip_parameter.ipindex
        dict['ipindex'] = ipindex
        dict['resultshow'] = ''
        repath="/Sharedvolume/static/media/" + str(fnrepjson['filename'])
        dict['resulpath'] =repath
        return render(request, "img_recognition.html", dict)

    else:
        dict = {}

        ipindex = ip_parameter.ipindex

        dict['ipindex'] = ipindex
        dict['resultshow'] = 'display: none;'
        dict['resulpath'] = '/Sharedvolume/static/home/img/team/team-01.jpg'
        dict['error'] = 'Image error! Please upload your image.'#dict['error'] = 'Remark or image error! Please try again.'
        return render(request, "img_recognition.html", dict)

class Get_ip_parameter:
    ip_server = load(req.urlopen('http://jsonip.com'))['ip']
    url = "http://" + str(ip_server) + ":8009/api/upload/"  # production
    filenameurl = "http://" + str(ip_server) + ":8009/api/getfilename/"
    recurl = "http://" + str(ip_server) + ":8009/api/image_recognition/"  # production
    ipindex = "http://" + str(ip_server) + ":8005/index/"
    def get_ip_parameter_test(self):
        self.url = "http://localhost:8009/api/upload/"  # local test
        self.filenameurl = "http://localhost:8009/api/getfilename/"
        self.recurl = "http://localhost:8009/api/image_recognition/"
        self.ipindex = "http://localhost:8005/index/"

