from django.shortcuts import render

# Create your views here.
def hello(request):
    #return HttpResponse("myapp2")
    return render(request, "hello.html")
