"""создание словаря"""
from collections import OrderedDict as od

usser1 = od()

usser1['age'] = '32'
usser1['first_name'] = 'veret'
usser1['last_name'] = 'alena'
usser1['city'] = 'novopolo'

for name, language in usser1.items():
    print(name.title() + ' = ' + language.title())









