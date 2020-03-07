from django.test import TestCase

# Create your tests here.
# nb!
from googletrans import Translator
translator = Translator()
print(translator.translate('').text)