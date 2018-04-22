from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from common.models import Users
from datetime import datetime

def index(request):
    ulist = Users.objects.all()
    context = {"userslist":ulist}
    return render(request,"myadmin/users/index.html",context)

def add(request):
    return render(request, "myadmin/users/add.html")

def insert(request):
    try:
        ob = Users()
        ob.username = request.POST['username']
        ob.name = request.POST['name']
        #md5加密
        import hashlib
        m = hashlib.md5()
        m.update(bytes(request.POST['password'],encoding="utf8"))
        ob.password = m.hexdigest()
        ob.sex = request.POST['sex']
        ob.address = request.POST['address']
        ob.code = request.POST['code']
        ob.phone = request.POST['phone']
        ob.email = request.POST['email']
        ob.state = 1
        ob.addtime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.save()
        context = {"info": "添加成功！"}
    except Exception as e:
        print(e)
        context = {"err":"添加失败！"}
    return render(request,"myadmin/info.html",context)


def edit(request,uid):
    pass
def update(request,uid):
    pass
def delete(request,uid):
    try:
        Users.objects.get(id = uid).delete()
        context = {"info": "删除成功！"}
    except Exception as e:
        print(e)
        context = {"info":"删除出错！"}
    return render(request,"myadmin/info.html",context)