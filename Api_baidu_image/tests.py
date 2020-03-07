from django.test import TestCase
import requests
import base64

# Create your tests here.
f = open('cat2.jpg', 'rb')
img = base64.b64encode(f.read())
host = 'https://aip.baidubce.com/rest/2.0/image-classify/v2/advanced_general'
headers={
   'Content-Type':'application/x-www-form-urlencoded'
}
access_token= '24.86363b027e8bf45d97a96aca7537604f.2592000.1586016738.282335-18692896'
host=host+'?access_token='+access_token

data={}
data['access_token']=access_token
data['image'] =img
#print(img)
res = requests.post(url=host,headers=headers,data=data)
req=res.json()
print(req['result'])
