from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def test(request):
    return HttpResponse("OK")

def create(request):
    return HttpResponse("OK2")
