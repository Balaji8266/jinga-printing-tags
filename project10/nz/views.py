from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def kane(request):
    return HttpResponse('<h1>kane mawaaa</h1>')

def rachin(request):
    return HttpResponse('<h1>One of The New Sensation for upcoming Generations </h1>')