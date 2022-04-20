import random

from django.shortcuts import render
#from django.http import HttpResponse
import random

def home(request):
    return render(request, 'generator/home.html')

def about(request):
    return render(request, 'generator/about.html')

def password(request):

    characters = list('abcdefghijklmnñopqrstuvwxyz')
    generated_password = ''

    uppercase_letters = list( map(lambda letter:letter.upper(),characters) )

    length = int(request.GET.get('length'))
    if request.GET.get('mayuscula'):
        characters.extend(uppercase_letters)
    if request.GET.get('special'):
        characters.extend(list('@+-*/_-!"#$%&()=?'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    for char in range(length):
        generated_password += random.choice(characters)

    return render(request, 'generator/password.html', {'password':generated_password})