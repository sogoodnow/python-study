from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from common.models import Users,Types,Goods
from django.core.paginator import Paginator

# 公共信息加载
def loadinfo(request):
    context = {}
    lists = Types.objects.filter(pid=0)
    print(lists)
    context['typelist'] = lists
    return context


# 用户登录
def login(request):
    return render(request,"web/login.html")

def dologin(request):
    # 校验验证码
    verifycode = request.session['verifycode']
    code = request.POST['code']
    if verifycode != code:
        context = {'info':'验证码错误！'}
        return render(request,"web/login.html",context)

    # 获取输入
    username = request.POST.get('username')
    # 密码处理
    import hashlib
    m = hashlib.md5()
    password = request.POST.get('password')
    m.update(bytes(password,encoding='utf8'))
    password = m.hexdigest()
    # 获取数据
    try:
        user =Users.objects.get(phone = username)
        if user.password == password and user.state != 0: # 不是管理员,登录成功加入session，并跳转首页
            request.session['vipuser'] = user.toDict()
            return redirect(reverse("index"))
        else:
            context = {"info": "登录失败"}
            return render(request, "web/login.html", context)
    except Exception as e:
        context = {"info": "发生异常！"+e}
        return render(request, "web/login.html", context)

def logout(request):
    del request.session['vipuser']
    return redirect(reverse("login"))

# 用户注册
def register(request):
    return render(request,"web/register.html")

def doregister(request):
    # 获取注册信息
    username = request.POST.get('username')
    password = request.POST.get('password')
    repassword = request.POST.get('repassword')
    # 判断两次密码输入是否一致
    if password != repassword:
        context = {"info":"密码输入不一致"}
        return render(request,"web/register.html",context)
    else:
        try:
            # 判断用户是否存在
            count = Users.objects.filter(phone = username ).count()
            print(count)
            if count > 0:
                context = {"info": "用户已存在"}
                return render(request, "web/register.html",context)
            else:
                # 添加数据进入模型
                user = Users()
                user.phone = username
                user.username = username
                # 密码处理
                import hashlib
                m = hashlib.md5()
                m.update(bytes(password, encoding='utf8'))
                user.password = m.hexdigest()
                user.save()
                # 完成后跳转至登录页面
                context = {"info": "注册完成，请登录"}
                return render(request, "web/login.html", context)
        except Exception as e:
            context = {"info": "注册失败"+e}
            return render(request, "web/register.html", context)



def index(request):
    context = loadinfo(request)
    return render(request,"web/index.html",context)

def plists(request,pIndex=1):
    # 获取商品
    goods = Goods.objects
    context = loadinfo(request)
    # mywhere = []  # 定义一个用于存放搜索条件列表
    # 获取页面传递的类别id，空则为0
    typeid = int(request.GET.get('typeid',0))
    context["tid"] = typeid
    # print(typeid)
    if typeid >0:
        # 类别id不为空，则获取对应类别所有商品
        # select id from types where pid='参数id'  select * from goods where typeid in [query1]
        plist = goods.filter(typeid__in=Types.objects.only('id').filter(pid=typeid))

    else:
        plist = goods.filter()
    context['goodslist'] = plist

    # 获取、判断并封装关keyword键搜索
    # kw = request.GET.get("typeid", None)
    # if kw:
    #     # 查询商品名中只要含有关键字的都可以
    #     plist = plist.filter(typeid__contains=kw)
    #     mywhere.append("typeid=" + kw)

    # 执行分页处理
    pIndex = int(pIndex)
    page = Paginator(plist,2)
    max_page = page.num_pages
    # 越界判断
    if pIndex > max_page:
        pIndex = max_page
    if pIndex<1:
        pIndex = 1
    # 当前页数据
    current_list = page.page(pIndex)
    # 页码列表
    page_list = page.page_range
    # 设置返回值
    context["pIndex"] = pIndex
    context["current_list"] = current_list
    context["page_list"] = page_list
    context["max_page"] = max_page
    # context["mywhere"] = mywhere
    return render(request, "web/list.html",context)

def detail(request,gid):
    context = loadinfo(request)
    ob = Goods.objects.get( id = gid)
    ob.clicknum +=1
    ob.save()
    context['goods'] = ob
    return render(request, "web/detail.html",context)