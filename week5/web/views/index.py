from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("网站前台管理！")