from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from common.models import Users


# Create your views here.
def verify(request):
    return render(request,"myadmin/index.html")

def index(request):
    return render(request,"myadmin/index.html")

def login(request):
    # 登录页面
    return render(request,"myadmin/login.html")

def dologin(request):
    # 执行登录
    try:
        print(request.POST.get('username'))
        ob = Users.objects.get(username= request.POST["username"])
        if ob.state == 0: # 是否为管理员
            # 密码判断
            import hashlib
            m = hashlib.md5()
            m.update(bytes(request.POST['password'], encoding="utf8"))
            print(m.hexdigest())
            if ob.password == m.hexdigest():
                # 加入session
                request.session["adminuser"] = ob.toDict()
                print("ok")
                return redirect(reverse("myadmin_index"))
            else:
                context = {"info": "密码错误"}
        else:
            context = {"info":"此用户非管理员"}
    except Exception as err:
        print(err)
        context = {"info":"登录账号不存在"}
    return render(request,"myadmin/login.html",context)

def logout(request):
    # 执行退出
    del request.session["adminuser"]
    return redirect(reverse("myadmin_login"))