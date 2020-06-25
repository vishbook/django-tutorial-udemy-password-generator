from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
    return render(request, 'generator/home.html', {'pass':'jhjkghfg'})

def about(request):
    return render(request, 'generator/about.html')

def password(request):
    genpass = ''
    characters = list('abcdefghijklmnopqrstuvwxyz')
    
    if request.GET.get('uppercase'):
        characters.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    if request.GET.get('specials'):
        characters.extend('!#$%^&*()')

    if request.GET.get('numbers'):
        characters.extend('0123456789')
    
    length = int(request.GET.get('length',12))
    for x in range(length):
        genpass += random.choice(characters)
    return render(request, 'generator/pass.html', {'password':genpass})