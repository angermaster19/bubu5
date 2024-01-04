from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,"index.html")

def page(request):
    return render(request, "page.html")

def love(request):
    return render(request,"love.html")

def page2(request):
    return render(request,"test.html")