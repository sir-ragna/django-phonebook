from django.http import HttpResponse
from django.shortcuts import render

def index(request):

    #return HttpResponse("<h1>Hello world</h1>")

    return render(request, "frontpage.html.j2")