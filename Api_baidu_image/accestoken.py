from urllib import request
import ssl
import json
def accestoken():
    gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
    # client_id : AK， client_secret : SK
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_' \
           'type=client_credentials&client_id=mgVMB10Aqnn24WqrBpoL1528&client_secret=15GyuqRaVUTO1waOiHGm8akGmAP1B3x3'
    req = request.Request(host)
    response = request.urlopen(req, context=gcontext).read().decode('UTF-8')
    accresult = json.loads(response)
    return accresult

res=accestoken()
print(res)