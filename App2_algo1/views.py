from django.shortcuts import render
import os
# Create your views here.
def algo1(request):
    #return HttpResponse("myapp2")

    category="cat"

    return render(request, "algo1.html",{"data":category})

def algo1_upload(request):

    File = request.FILES.get("myfile", None)
    image_path = "./App2_algo1/images/"+"%s"%File.name #+ "%s" % File.name

    # open file to write
    with open(image_path, 'wb+') as f:
        # Write to file in chunks
        for chunk in File.chunks():
            f.write(chunk)
    c="humen"
    return render(request, "algo1.html",{"data":c})#,locals())
