from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def virat(request):
    return HttpResponse('<h1>Chase Master Chased The Master......</h1>')


def sachin(request):
    return HttpResponse('<h1>Master Blaster Sachin Ramesh Tendulkar</h1>')