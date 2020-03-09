from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from json import load
from urllib import request as req
# Create your views here.


def login(request):
    #return HttpResponse("myapp2")
    return render(request, "login.html")

def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('form-username', '')
        password = request.POST.get('form-password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user) # 登录
            request.session['user'] = username # 将session信息记录到浏览器
            response = HttpResponseRedirect('/index/')
            return response
            #return render(request,'index.html')
        else:
            return render(request,'login.html', {'error': 'username or password error!'})
    else:
        return render(request,'login.html')

def index(request):
    #return HttpResponse("myapp2")

    #ip1=req.urlopen('http://ip.42.pl/raw').read()
    ip1 = load(req.urlopen('http://jsonip.com'))['ip']
    #ip1="localhost"
    #print(ip1)
    ip1="http://"+str(ip1)+":8001/img_rec/"
    return render(request, "index.html",{'ipimgrec': ip1})

def index_action(request):
    #return HttpResponse("myapp2")

    response = HttpResponseRedirect('/img_rec/')
    return response
