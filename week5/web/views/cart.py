from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from common.models import Users,Types,Goods



# 公共信息加载
def loadinfo(request):
    context = {}
    lists = Types.objects.filter(pid=0)
    print(lists)
    context['typelist'] = lists
    return context



def index(request):
    context = loadinfo(request)
    if 'shoplist' not in request.session:
        request.session['shoplist'] = {}
    return render(request,"web/cart.html",context)

def add(request,gid):
    goods = Goods.objects.get(id=gid)
    goods_buy = goods.toDict()
    goods_buy['m'] = int(request.POST.get('m',1))
    shoplist = request.session.get('shoplist',{})
    if gid in shoplist:
        shoplist[gid]['m']+= goods_buy['m']
    else:
        shoplist[gid] = goods_buy
    request.session['shoplist'] = shoplist
    return redirect(reverse('cart_index'))

def delete(request,gid):
    shoplist = request.session['shoplist']
    del shoplist[gid]
    request.session['shoplist'] = shoplist
    return redirect(reverse('cart_index'))

def clear(request):
    request.session['shoplist'] = {}
    return redirect(reverse('cart_index'))

def change(request):
    shoplist = request.session['shoplist']
    gid = request.GET.get('gid',0)
    num = int(request.GET.get('num',1))
    if num<1:
        num = 1
    shoplist[gid]['m'] = num
    request.session['shoplist'] = shoplist
    return redirect(reverse('cart_index'))