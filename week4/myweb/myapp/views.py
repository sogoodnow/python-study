from django.shortcuts import render,HttpResponse,reverse,redirect
from django.http import JsonResponse
from django.conf import settings
from . models import *
from PIL import Image
from django.core.paginator import Paginator
import os,time
# Create your views here.
def index(request):
    return render(request, "index.html")

def picdel(request,pid):
    pic = Pics.objects.get(id=pid)
    sname = "static/"+pic.spicname
    bname = "static/"+pic.bpicname
    try:
        if os.path.exists(sname):
            os.remove(sname)
        if os.path.exists(bname):
            os.remove(bname)
        pic.delete()
        return HttpResponse("图片删除成功！")
    except:
        return HttpResponse("图片删除失败！")

def picupdata(request,pid = 0):
    # 根据图片id检索数据库该图片信息
    if request.method=="GET":
        pid = request.GET["pid"]
        pictitle = request.GET["pictitle"]
        bpicname = request.GET["bpicname"]
        content = {"pid":pid, "pictitle":pictitle, "bpicname":bpicname}
        # 跳转至更新上传页面
        return render(request,"users/picupdata.html",content)
    else:
        # 获取当前时间
        time_now = int(time.time())
        time_local = time.localtime(time_now)
        da = time.strftime("%Y-%m-%d-%H-%M-%S", time_local)

        # 获取该图片原来的数据库信息
        pic = Pics.objects.get(id = pid)

        # 更新图片标题
        pic.pictitle = request.POST["pictitle"]
        uid = pic.uid # 用户id，用于图片名称规则

        # 获取上传文件
        myfile = request.FILES.get("picname", None)
        if not myfile:  # 文件为空
            return HttpResponse("没有文件！")

        # 文件名称的定义：学员id+当前时间+文件后缀
        print(str(myfile))
        # 文件名规则为用户id+“_”+时间
        filename = str(uid) + '_' + str(da) + '.' + myfile.name.split('.').pop()
        # 保存文件至服务器stati/img目录
        try:
            # 保存操作
            savepath = open('./static/img/' + filename, 'wb+')
            for ch in myfile.chunks():
                savepath.write(ch)
            savepath.close()
            # 生成小图操作
            im = Image.open("./static/img/" + filename)
            im.thumbnail((75, 75))
            im.save("./static/img/s_" + filename)

            # 保存成功后，更新数据库
            pic.bpicname = 'img/' + filename
            pic.spicname = 'img/s_' + filename
            pic.updatetime = da
            pic.uid = uid
            pic.save()
            return redirect(reverse("piclist",args=(uid,)))
        except Exception as e:
            return HttpResponse("文件保存失败！" + e)



def piclist(request,uid):
    pics = Pics.objects.all().filter(uid = uid)
    content = {"pics":pics}

    return  render(request,"users/piclist.html",content)


def picupload(request,uid=0):
    print(uid)
    return render(request,"users/picupload.html",{"uid":uid})

def savefile(request,uid):

    # 获取当前时间
    time_now = int(time.time())
    time_local = time.localtime(time_now)
    da = time.strftime("%Y-%m-%d-%H-%M-%S",time_local)
    # 获取页面上的学员id
    if uid!=0:
        # 获取图片标题
        title = request.POST["pictitle"]
        # 获取上传文件
        myfile = request.FILES.get("picname",None)
        if not myfile:  # 文件为空
            return HttpResponse("没有文件！")
        # 文件名称的定义：学员id+当前时间+文件后缀
        filename = str(uid)+'_'+str(da)+'.'+myfile.name.split('.').pop()
        # 保存文件至服务器stati/img目录
        try:
            # 保存操作
            savepath = open('./static/img/'+filename,'wb+')
            for ch in myfile.chunks():
                savepath.write(ch)
            savepath.close()
            # 生成小图操作
            im = Image.open("./static/img/" + filename)
            im.thumbnail((75, 75))
            im.save("./static/img/s_" + filename)
            # 保存成功后，将信息存入数据库
            pic = Pics()
            pic.pictitle = title
            pic.bpicname = 'img/'+filename
            pic.spicname = 'img/s_'+filename
            pic.updatetime = da
            pic.uid = uid
            pic.save()
        except Exception as e:
            return HttpResponse("文件保存失败！"+e)
        # 操作完成后
        return render(request, "users/picupload.html",{"uid":uid})
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
