from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello(request, id):
    return HttpResponse('Hello World ' + str(id))