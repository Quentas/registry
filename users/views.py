from django.shortcuts import redirect, render, get_object_or_404
import sys, os, inspect
import json
from .models import UserData, City
from allauth.socialaccount.models import SocialAccount 
from django.http import HttpResponse
from django.template import RequestContext, Template
from register.settings import KOSTYL

def preview_form(request):
    if request.user.is_anonymous:
        return redirect('base_page')
    city = request.POST['city_name']
    city = City.objects.get(id=city)
    full_username = SocialAccount.objects.get(user=request.user).extra_data['name']
    return render(request, 'side_templates/preview_form.html', {'city': city, 'full_username' : full_username})

def base_page(request):
    if not request.user.is_anonymous:
        return redirect('create_form')
    return render(request, 'base.html')

def create_form(request):
    if request.user.is_anonymous:
        return redirect('base_page')
    full_username = SocialAccount.objects.get(user=request.user).extra_data['name']
    return render(request, 'side_templates/form.html', {
        'full_username' : full_username
    })

def home (request):
	return redirect('base_page')

def choose_city(request):
    if request.user.is_anonymous:
        return redirect('base_page')
    if request.method == 'POST':
        searched = request.POST['searched']
        cities = City.objects.filter(name__startswith=searched)
        return render(request, 'side_templates/choose_city.html', {'cities': cities, 'searched' : searched})
    else:
        return render(request, 'side_templates/choose_city.html', {})

def save_form(request):
    if request.user.is_anonymous:
        return redirect('base_page')
    city = request.POST['city_name']
    city = City.objects.get(id=city)
    user = get_object_or_404(SocialAccount, id=int(request.user.id)-KOSTYL) 
    '''
        id=x-1 because in SocialAccount table user_id != user _id in auth.users table
    '''
    UserData.objects.create(user = user, city = city)
    return redirect('success')

def success(request):
    return render(request, 'side_templates/success.html', {})

