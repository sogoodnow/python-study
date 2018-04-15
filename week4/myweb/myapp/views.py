from django.shortcuts import render,HttpResponse,reverse,redirect
from django.http import JsonResponse
from . models import *
from PIL import Image
from django.core.paginator import Paginator
import os,time
# Create your views here.
def index(request):
    return render(request, "index.html")

def piclist(request,uid=0):
    print(uid)
    return render(request,"users/piclist.html",{"uid":str(uid)})

def savefile(request,uid=0):
    if uid!=0:
        myfile = request.FILES.get("picname",None)
        if not myfile:
            return HttpResponse("没有文件！")
        filename = str(uid)+'_'+str(time.time())+'.'+myfile.name.split('.').pop()
        try:
            savepath = open('./static/img/'+filename,'wb+')
            for ch in myfile.chunks():
                savepath.write(ch)
            savepath.close()
            print(os.path.dirname(os.path.abspath(__file__)))
        except IOError:
            return HttpResponse("文件保存失败！"+IOError)
        im = Image.open("./static/img/"+filename)
        im.thumbnail((75,75))
        im.save("./static/img/s_"+filename)
        return render(request, "users/piclist.html")
    else:
        return HttpResponse("没有该学生图库")

def usermain(request, pIndex=1):
    try:
        userinfo = Userinfo.objects.all()  #获取所有表数据，装入模板，注意：取出时为列表
        p = Paginator(userinfo, 5)
        if pIndex == '':
            pIndex = '1'
        pIndex = int(pIndex)
        plist = p.page(pIndex)
        pnums = p.page_range
        p.num_pages
        # context为字典类型
        context = {"info":userinfo}
        return render(request, "users/main.html", {'plist': plist, 'pnums': pnums, 'pIndex': pIndex})
    except Exception as e:
        return HttpResponse("error:"+str(e))

def stuedit(request,uid=0):
    print(uid)
    if uid==0:
        return render(request, "users/stuedit.html")
    else:
        try:
            stu = Userinfo.objects.get(id=uid)
            # print(stu)
            content={"id":stu.id,"name":stu.name,"age":stu.age,"phone":stu.phone,"sex":stu.sex,"classname":stu.classname}
            # print(content)
            return render(request, "users/stuedit.html",content)
        except:
            content = {"info":"数据获取失败"}
            return render(request, "users/stuedit.html", content)

def studel(request,uid):
    # print(uid)
    stu = Userinfo.objects.get(id=uid)
    try:
        # 页面获取字段并加入模型保存
        stu.delete()
        context = {'info': '删除成功！'}
    except Exception as e:
        print(e)
        context = {'info': '删除失败！'}
    # return redirect(reverse("main"),context)
    return JsonResponse(context)
    # return render(request, "users/main.html", context)

def stuadd(request):
    """
    新增用户
    :param request:
    :return:
    """
    # print(uid)
    if request.method=="POST" :
    # 新建模型类
        mod = Userinfo()
        # print(uid)
        try:
            # 页面获取字段并加入模型保存
            mod.name = request.POST.get("name")
            mod.age = request.POST.get("age")
            mod.phone = request.POST.get("phone")
            mod.sex = request.POST.get("sex")
            mod.classname = request.POST.get("classname")
            # print(mod.name,mod.age,mod.phone,mod.sex,mod.classname)
            mod.save()
            context = {'info': '添加成功！'}
        except Exception as e:
            print(e)
            context = {'info': '添加失败！'}
        return JsonResponse(context)
    else:
        # print(uid)
        try:
            uid = request.GET.get("uid")
            stu = Userinfo.objects.get(id=uid)
            stu.name = request.GET["name"]
            stu.age = request.GET["age"]
            stu.sex = request.GET["sex"]
            stu.phone = request.GET["phone"]
            stu.classname = request.GET["classname"]
            stu.save()
            context = {'info': '更新成功！'}
            return JsonResponse(context)
        except Exception as e:
            print(e)
            context = {'info': '更新失败！'}
            return JsonResponse(context)
