from .views import *
from django.urls import path, include
from .service import ping
urlpatterns = [
    path('preview_form/', preview_form, name='preview_form'),
    path('save_form', save_form, name='save_form'),
    path('base_page', base_page, name='base_page'),
    path('', home, name='home'),
    path('create_form', create_form, name='create_form'),
    path('choose_city', choose_city, name='choose_city'),
    path('success', success, name='success'),
    path('testing/ping', ping),
]
