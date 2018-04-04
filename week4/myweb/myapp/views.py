from django.shortcuts import render
from django.http import HttpResponse
from . models import Stu
# Create your views here.
def index(request):
    return HttpResponse("hello all!")

def stu(request):
    mod =Stu.objects
    aa = mod.get(id=73)
    print(aa)
    return  HttpResponse(aa)