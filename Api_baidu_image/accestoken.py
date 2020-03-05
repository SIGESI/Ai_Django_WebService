from urllib import request
import ssl
import json
gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
# client_id 为官网获取的AK， client_secret 为官网获取的SK
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_' \
       'type=client_credentials&client_id=mgVMB10Aqnn24WqrBpoL1528&client_secret=15GyuqRaVUTO1waOiHGm8akGmAP1B3x3'
req = request.Request(host)
response = request.urlopen(req, context=gcontext).read().decode('UTF-8')
result = json.loads(response)
if (result):
    print(result)
