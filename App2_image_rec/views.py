from django.shortcuts import render
import os
from json import load
from urllib import request as req
import requests
import json
# Create your views here.
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def img_rec(request):
    #return HttpResponse("myapp2")

    ipindex = load(req.urlopen('http://jsonip.com'))['ip']
    ipindex = "http://" + str(ipindex) + ":8005/index/"
    dict={ 'ipindex': ipindex,'resultshow':'display: none;', 'resulpath':'/Sharedvolume/static/home/img/team/team-01.jpg'}
    #tkey = request.session.session_key
    #ramark='cat'
    #tkey=ramark+tkey
    #print(tkey)
    return render(request, "img_recognition.html", dict)
@login_required
def img_rec_action(request):
    ipindex = load(req.urlopen('http://jsonip.com'))['ip']
    if (request.FILES.get("file", None)) and (request.POST.get("remark")) is not None:
        url = "http://" + str(ipindex) + ":8009/api/upload/"  # production
        # url = "http://localhost:8000/api/upload/"  # local test, Commented out in production
        # url = "http://15.236.92.5:8009/api/upload/"  # production
        remark = request.POST.get("remark")
        sessionkey = request.session.session_key
        remark = remark + sessionkey
        fileDic = {'file': request.FILES.get("file", None)}
        rmarkDic = {'remark': remark}  # post.get -> WSGI request

        requests.post(url, data=rmarkDic, files=fileDic)

        filenameurl = "http://" + str(ipindex) + ":8009/api/getfilename/"
        fnrep = requests.get(filenameurl, data=rmarkDic)
        fnrepjson = fnrep.json()

        recurl = "http://" + str(ipindex) + ":8009/api/image_recognition/"  # production
        # recurl = "http://localhost:8000/api/image_recognition/"
        # recurl = "http://15.236.92.5:8009/api/image_recognition/"

        rep = requests.get(recurl, data=rmarkDic)
        dict = {}
        resjson = rep.json()

        for i in range(5):
            # keyword[i]= resjson['result'][i]['keyword']
            # root[i]= resjson['result'][i]['root']
            # score[i]= resjson['result'][i]['score']
            dict['keyword' + str(i + 1)] = resjson['result'][i]['keyword']
            dict['root' + str(i + 1)] = resjson['result'][i]['root']
            dict['score' + str(i + 1)] = resjson['result'][i]['score']

        ipindex = "http://" + str(ipindex) + ":8005/index/"
        dict['ipindex'] = ipindex
        dict['resultshow'] = ''
        dict['resulpath'] = '/media/' + str(fnrepjson['filename'])
        return render(request, "img_recognition.html", dict)

    else:
        dict = {}

        ipindex = "http://" + str(ipindex) + ":8005/index/"
        dict['ipindex'] = ipindex
        dict['resultshow'] = 'display: none;'
        dict['resulpath'] = '/Sharedvolume/static/home/img/team/team-01.jpg'
        dict['error'] = 'Remark or file error! Please try again.'
        return render(request, "img_recognition.html", dict)


'''
@login_required
def img_rec_action(request):

    ipindex = load(req.urlopen('http://jsonip.com'))['ip']

    url = "http://" + str(ipindex) + ":8009/api/upload/"  # production
    #url = "http://localhost:8000/api/upload/"  # local test, Commented out in production
    #url = "http://15.236.92.5:8009/api/upload/"  # production
    remark=request.POST.get("remark")
    
    
    sessionkey = request.session.session_key
    remark=remark+sessionkey
    fileDic = {'file': request.FILES.get("file", None)}
    rmarkDic = {'remark': remark}  # post.get -> WSGI request

    requests.post(url, data=rmarkDic, files=fileDic)

    filenameurl="http://" + str(ipindex) + ":8009/api/getfilename/"
    fnrep= requests.get(filenameurl, data=rmarkDic)
    fnrepjson=fnrep.json()

    recurl = "http://" + str(ipindex) + ":8009/api/image_recognition/"  # production
    #recurl = "http://localhost:8000/api/image_recognition/"
    #recurl = "http://15.236.92.5:8009/api/image_recognition/"

    rep = requests.get(recurl, data=rmarkDic)
    dict = {}
    resjson = rep.json()

    for i in range(5):
        # keyword[i]= resjson['result'][i]['keyword']
        # root[i]= resjson['result'][i]['root']
        # score[i]= resjson['result'][i]['score']
        dict['keyword' + str(i+1)] = resjson['result'][i]['keyword']
        dict['root' + str(i+1)] = resjson['result'][i]['root']
        dict['score' + str(i+1)] = resjson['result'][i]['score']

    ipindex = "http://" + str(ipindex) + ":8005/index/"
    dict['ipindex'] = ipindex
    dict['resultshow'] = ''
    dict['resulpath'] = '/media/'+str(fnrepjson['filename'])
    return render(request, "img_recognition.html", dict)
'''