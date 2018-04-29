from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from common.models import Types,Users
from datetime import datetime
from django.core.paginator import Paginator


def index(request,pIndex = 1):
    ulist = Types.objects.extra(select = {'_has':'concat(path,id)'}).order_by('_has')
    for ob in ulist:
        ob.pname = ".  .  .  ."*(ob.path.count(',')-1)
    context = {'plist': ulist}
    return render(request, "myadmin/types/index.html", context)

def add(request,tid):
    if tid == '0':
        context = {"pid":'0',"path":'0,',"name":"根类别"}
    else:
        ob = Types.objects.get(id = tid)
        context = {"pid": ob.id, "path": ob.path+str(ob.id)+',', "name": ob.name}
    return render(request, "myadmin/types/add.html",context)

def insert(request):
    try:
        ob = Types()
        ob.name = request.POST['name']
        ob.pid = request.POST['pid']
        ob.path = request.POST['path']
        ob.save()
        context = {"info": "添加成功！"}
    except Exception as e:
        print(e)
        context = {"err":"添加失败！"}
    return render(request,"myadmin/info.html",context)


def edit(request,tid):
    try:
        ob = Types.objects.get(id = tid)
        context = {"type": ob}
        return render(request, "myadmin/types/edit.html", context)
    except Exception as e:
        print(e)
        context = {"info":"修改出错！"}
        return render(request,"myadmin/info.html",context)


def update(request,tid):
    try:
        ob = Types.objects.get(id=tid)
        ob.name = request.POST['name']
        ob.save()
        context = {"info": "编辑成功！"}
    except Exception as e:
        print(e)
        context = {"err":"编辑失败！"}
    return render(request,"myadmin/info.html",context)

def delete(request,tid):
    # 判断是否有子类别存在，若存在则无法删除
    count = Types.objects.filter(pid = tid).count()
    if count>0:
        context = {"info": "有子类项目，无法删除！"}
        return render(request, "myadmin/info.html", context)
    try:
        Types.objects.get(id = tid).delete()
        context = {"info": "删除成功！"}
    except Exception as e:
        print(e)
        context = {"info":"删除出错！"}
    return render(request,"myadmin/info.html",context)
