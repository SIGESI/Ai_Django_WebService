from django.test import TestCase
#from  Api_upload.models import File
# Create your tests here.
import requests

fndic={'filename':'bid'}
recurl = "http://localhost:8000/api/getfilename/"
rep = requests.get(recurl, data=fndic)

print(rep)