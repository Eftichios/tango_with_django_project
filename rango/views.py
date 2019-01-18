from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    # construc the context dictionary to be passed to the template
    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}

    # return a rendered response to send to the client
    return render(request, 'rango/index.html', context=context_dict)


def about(request):
    return HttpResponse("Rango says here is the about page! <br/><a href='/rango/'>Index</a>")
