from aip import AipImageClassify
import base64

APP_ID = '18692896'
API_KEY = 'mgVMB10Aqnn24WqrBpoL1528'
SECRET_KEY = '15GyuqRaVUTO1waOiHGm8akGmAP1B3x3'

client = AipImageClassify(APP_ID, API_KEY, SECRET_KEY)

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_file_content('tiger.jpg')
img = base64.b64encode(image)

print(client.advancedGeneral(image))
