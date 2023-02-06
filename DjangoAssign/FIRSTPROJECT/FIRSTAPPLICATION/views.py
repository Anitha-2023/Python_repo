from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("My First DJANGO Application !!!")

def appindex(request):
    return render(request,"FIRSTAPPLICATION/index.html")