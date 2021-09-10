import sys, os, inspect
import json
from users.models import User, City
import django


import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "register.settings")
django.setup()

def upload_from_file():
    currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    parentdir = os.path.dirname(currentdir)
    file = parentdir + '\\example.json'
    with open(file, 'r', encoding ="utf8") as f:
        obj = json.loads(f.read())
        for i in obj:
            city_name = i['Назва об\'єкта українською мовою']
            layer1 = i['Перший рівень']
            layer2 = i['Другий рівень']
            layer3 = i['Третій рівень']
            layer4 = i['Четвертий рівень']
            city_category = i['Категорія']
            print(city_name, layer1, city_category)
            City.objects.create(
                name=city_name,
                first_layer=layer1, 
                second_layer=layer2,
                third_layer=layer3,
                fourth_layer=layer4,
                category=city_category
                )
    

upload_from_file()