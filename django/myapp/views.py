from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello(request):
    return HttpResponse('Hello World')

def index(request):
    id = ''
    even = {
        'GG',
        'Good',
        'ping',
        }

    return render(request, 'index.html', {
        'id': id,
        'even': even,
    })