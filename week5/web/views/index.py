from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,"web/index.html")

def plists(request):
    print("ok")
    return render(request, "web/list.html")

def detail(request):
    return render(request, "web/detail.html")