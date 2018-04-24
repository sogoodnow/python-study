from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,"myadmin/index.html")

def login(request):
    # 登录页面
    return render(request,"myadmin/login.html")

def dologin(request):
    # 执行登录
    pass

def logout(request):
    # 执行退出
    pass