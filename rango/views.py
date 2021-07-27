from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    #chapter 3:
    # html="<html> <body><a href='/rango/about/'>About</a></br><p>Rango says hey there partner!</p></body></html>"
    # return HttpResponse(html)
    #chapter 4:
    context_dict={'boldmessage':'Crunchy,creamy,cookie,candy,cupcake!'}
    return render(request,'rango/index.html',context=context_dict)

def about(request):
    html="<html> <body><a href='/rango/'>Index</a></br><p>Rango says here is the about page.</p></body></html>"
    return HttpResponse(html)
    
