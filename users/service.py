import sys, os, inspect
from .models import City
import json
from django.http import JsonResponse

def ping(request):
    '''For testing
    '''
    data = {'ping': 'pong!'}
    return JsonResponse(data)

def upload_from_file():
    '''Moves all entries from json file to users_city table
    '''
    file = 'cities.json'
    with open(os.path.join(sys.path[0], file), 'r', encoding ="utf8") as f:
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
    