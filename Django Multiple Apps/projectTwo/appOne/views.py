from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def d1(request):

    return HttpResponse("<h1>Hello Django</h1>")
