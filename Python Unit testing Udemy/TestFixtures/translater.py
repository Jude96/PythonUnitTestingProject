#import googletrans

from googletrans import Translator
translator = Translator()
"""
translator.translate('안녕하세요.')
# <Translated src=ko dest=en text=Good evening. pronunciation=Good evening.>
translator.translate('안녕하세요.', dest='ja')
# <Translated src=ko dest=ja text=こんにちは。 pronunciation=Kon'nichiwa.>
translator.translate('veritas lux mea', src='la')
# <Translated src=la dest=en text=The truth is my light pronunciation=The truth is my light>

#translator.translate('Bienvenue')
"""
s = translator.detect('이 문장은 한글로 쓰여졌습니다.')

text1 = 'Ta peau sur ma peau ca leur fait peur'
ttext2 = 'Tes lèvres sur mes lèvres est la plus belle chose'

p = translator.translate(text=ttext2, dest= 'en')

print(f'The translated text is:- {p.text}')

print(f'Confidence level:- {p.extra_data}')

print(type(p))

print(p)

print(s)

