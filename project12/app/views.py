from django.shortcuts import render

# Create your views here.

def conditional(request):
    d={'a':100}
    return render(request,'conditional.html', d)
