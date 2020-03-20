from django.test import TestCase
#from  Api_upload.models import File
# Create your tests here.
import requests

fndic={'remark':'bid'}
recurl = "http://localhost:8005/api/getfilename/"
rep = requests.get(recurl, data=fndic)

print(rep)

repj=rep.json()
print(repj)
repstr=str(repj['filename'])
print(repstr)
repath = "/media/" + str(repj['filename'])
print(repath)
dict = {}
dict['resulpath'] =repath
print(dict)
