from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # construct the context dictionary to be passed to the template
    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}

    # return a rendered response to send to the client
    return render(request, 'rango/index.html', context=context_dict)


def about(request):
    # return a rendered response to send to the client
    return render(request, 'rango/about.html', context={})
