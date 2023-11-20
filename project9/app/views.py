from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def virat(request):
    return render(request,'virat.html')

def siraj(request):
    return HttpResponse('<h1><marquee>The Hyderabadi Star SIRAJ BHAI</marquee></h1>')