from django.shortcuts import render

# Create your views here.
def login(request):
    context = {}
    return render(request, 'layout/login.html', context)

def utp(request):
    context = {}
    return render(request, 'layout/utp.html', context)