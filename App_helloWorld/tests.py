from django.test import TestCase
import requests

# Create your tests here.
# nb!
from googletrans import Translator
translator = Translator()
print(translator.translate('').text)

rmarkDic = {"remark": "tiger" }

recurl="http://localhost:8000/api/image_recognition/"
rep=requests.get(recurl,data=rmarkDic)

print(rep.json())