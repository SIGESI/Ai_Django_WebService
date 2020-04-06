from django.test import TestCase
import requests
import base64
from googletrans import Translator

# Create your tests here.
f = open('dog.jpg', 'rb')
img = base64.b64encode(f.read())
host = 'https://aip.baidubce.com/rest/2.0/image-classify/v2/advanced_general'
headers={
   'Content-Type':'application/x-www-form-urlencoded'
}
access_token= '24.360c74017f8ebddeebb228841fa6e186.2592000.1588725752.282335-18692896'
host=host+'?access_token='+access_token

data={}
data['access_token']=access_token
data['image'] =img
#print(img)
res = requests.post(url=host,headers=headers,data=data)
req=res.json()

#print(req)

translator = Translator()
for i in range(5):
   req['result'][i]['root']=translator.translate(req['result'][i]['root']).text
   req['result'][i]['keyword']=translator.translate(req['result'][i]['keyword']).text
print(req['result'])
