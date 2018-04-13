from django.shortcuts import render,HttpResponse,reverse,redirect
from . models import *
# Create your views here.
def index(request):
    return render(request, "index.html")


def usermain(request):
    try:
        userinfo = Userinfo.objects.all()  #获取所有表数据，装入模板，注意：取出时为列表
        # context为字典类型
        context = {"info":userinfo}
        return render(request, "users/main.html", context)
    except Exception as e:
        return HttpResponse("error:"+str(e))

def stuedit(request):
    return render(request, "users/stuedit.html")

def stusave(request):

    print("inininiininin")
    # context为字典类型
    # context = {"info": userinfo}
    mod = Userinfo.objects
    ls = request["data"]
    mod.name = ls["name"]
    content = {"aa":mod.name}
    print(mod.name+"dfdfdfdfdfdfdfdfdfdf")
    return render(request, "users/stuedit.html", content)