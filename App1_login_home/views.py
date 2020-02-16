from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth

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