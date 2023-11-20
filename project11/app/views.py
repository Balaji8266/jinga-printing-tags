from django.shortcuts import render

# Create your views here.

def siraj(request):
    d = {'username':'Balaji', 'age':20}
    return render(request,'siraj.html', context=d)
