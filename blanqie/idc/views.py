from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'idc/home.html')

def learn(request):
    return render(request, 'idc/learn.html')

def test(request):
    return render(request, 'idc/test.html')