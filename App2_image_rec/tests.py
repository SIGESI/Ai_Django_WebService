from django.test import TestCase
import random
from json import load
from urllib import request as req
import requests
# Create your tests here.
#key = request.session.session_key
#print(key)
'''

dict={}
fnrepjson="bird_rOp2xjj.jpg"
dict['resulpath'] = '/media/' + str(fnrepjson)
print(dict)
'''
#remark=random.sample('zyxwvutsrqponmlkjihgfedcba',6)


#remark=''.join(random.sample(['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a'], 6))
#print(remark)

class Get_ip_parameter:
    ipindex = load(req.urlopen('http://jsonip.com'))['ip']
    url = "http://" + str(ipindex) + ":8009/api/upload/"  # production
    filenameurl = "http://" + str(ipindex) + ":8009/api/getfilename/"
    recurl = "http://" + str(ipindex) + ":8009/api/image_recognition/"  # production
    def get_ip_parameter_test(self):
        self.url = "http://localhost:8009/api/upload/"  # local test
        self.filenameurl = "http://localhost:8009/api/getfilename/"
        self.recurl = "http://localhost:8009/api/image_recognition/"


ip_parameter=Get_ip_parameter()
ip_parameter.get_ip_parameter_test()
ipindex = ip_parameter.ipindex
url=ip_parameter.url
filenameurl=ip_parameter.filenameurl
recurl=ip_parameter.recurl
print(ipindex)
print(url)
print(recurl)
print(filenameurl)