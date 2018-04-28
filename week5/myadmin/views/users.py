from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from common.models import Users
from datetime import datetime
from django.core.paginator import Paginator


def search(request,pIndex = 1):
    # 获取检索字段
    keyword = request.GET.get("keyword")
    sex = request.GET.get("sex")
    # 定义一个用于存放搜索条件列表
    mywhere = []
    # 性别有指定检索条件
    if sex != "2":
        ulist = Users.objects.all().filter(name__contains=keyword).filter(sex=sex)
    else:
        ulist = Users.objects.all().filter(name__contains=keyword)
    # 添加条件
    mywhere.append("keyword=" + keyword)
    mywhere.append("sex=" + sex)

    p = Paginator(ulist, 3)
    maxpages = p.num_pages
    if pIndex == '':
        pIndex = '1'
    pIndex = int(pIndex)
    # 页数阈值判断
    if pIndex > maxpages:
        pIndex = maxpages
    if pIndex < 1:
        pIndex = 1
    plist = p.page(pIndex)# 当前页数据
    pnums = p.page_range  # 页码列表
    context = {'plist': plist, 'pnums': pnums, 'pIndex': pIndex,'sex':sex,'mywhere':mywhere,'maxpages':maxpages}
    return render(request, "myadmin/users/index.html", context)

def index(request,pIndex = 1):
    ulist = Users.objects.all()
    p = Paginator(ulist, 3)
    if pIndex == '':
        pIndex = '1'
    pIndex = int(pIndex)
    plist = p.page(pIndex)
    pnums = p.page_range
    context = {'plist': plist, 'pnums': pnums, 'pIndex': pIndex}
    return render(request, "myadmin/users/index.html", context)

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
    try:
        ob = Users.objects.get(id = uid)
        context = {"user": ob}
        return render(request, "myadmin/users/edit.html", context)
    except Exception as e:
        print(e)
        context = {"info":"修改出错！"}
        return render(request,"myadmin/info.html",context)


def update(request,uid):
    try:
        ob = Users.objects.get(id=uid)
        ob.name = request.POST['name']
        ob.sex = request.POST['sex']
        ob.address = request.POST['address']
        ob.code = request.POST['code']
        ob.phone = request.POST['phone']
        ob.email = request.POST['email']
        ob.state = request.POST['state']
        ob.save()
        context = {"info": "编辑成功！"}
    except Exception as e:
        print(e)
        context = {"err":"编辑失败！"}
    return render(request,"myadmin/info.html",context)

def delete(request,uid):
    try:
        Users.objects.get(id = uid).delete()
        context = {"info": "删除成功！"}
    except Exception as e:
        print(e)
        context = {"info":"删除出错！"}
    return render(request,"myadmin/info.html",context)

def restpwd(request,uid):
    ob = Users.objects.get(id = uid)
    context = {"user":ob}
    return render(request,"myadmin/users/pwdedit.html",context)

def pwdupdate(request,uid):
    try:
        ob = Users.objects.get(id=uid)
        newpwd = request.POST['password1']
        import hashlib
        m = hashlib.md5()
        m.update(bytes(newpwd,encoding="utf8"))
        ob.password = m.hexdigest()
        ob.save()
        context = {"info": "更改成功！"}
    except Exception as e:
        print(e)
        context = {"info": "更改失败！"}
    return render(request,"myadmin/info.html",context)