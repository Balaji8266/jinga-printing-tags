from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def yuvaraj(request):
    return HttpResponse('<h1>The Undisputed Champion YuvaRaj Singh</h1>')


def sachin(request):
    return render(request, 'sachin.html')
