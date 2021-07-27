from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    html="<html> <body><a href='/rango/about'>About</a></br><p>Rango says hey there partner!</p></body></html>"
    return HttpResponse(html)

def about(request):
    html="<html> <body><a href='/rango/'>Index</a></br><p>Rango says here is the about page.</p></body></html>"
    return HttpResponse(html)
    
