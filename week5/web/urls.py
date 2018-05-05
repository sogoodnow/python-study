from django.conf.urls import url,include
from .views import index,cart,orders,vip

urlpatterns = [
    # 前台首页

    url(r'^$', index.index, name="index"),
    url(r'^detail/(?P<gid>[0-9]+)$', index.detail, name="pdetail"),#商品详情
    url(r'^list$', index.plists, name="list"),
    url(r'^list/(?P<pIndex>[0-9]+)$', index.plists, name="list"),

    # 会员登录
    url(r'^login$', index.login, name="login"),
    url(r'^dologin/$', index.dologin, name="dologin"),
    url(r'^logout/$', index.logout, name="logout"),
    url(r'^register/$', index.register, name="register"),
    url(r'^doregister/$', index.doregister, name="doregister"),

    # 购物车
    url(r'^cart$', cart.index, name="cart_index"),
    url(r'^cart/add(?P<gid>[0-9]+)$', cart.add, name="cart_add"),
    url(r'^cart/del(?P<gid>[0-9]+)$', cart.delete, name="cart_del"),
    url(r'^cart/clear$', cart.clear, name="cart_clear"),
    url(r'^cart/change$', cart.change, name="cart_change"),

    # 订单处理
    url(r'^orders/add$', orders.add, name='orders_add'),  # 订单的表单页
    url(r'^orders/confirm$', orders.confirm, name='orders_confirm'),  # 订单确认页
    url(r'^orders/insert$', orders.insert, name='orders_insert'),  # 执行订单添加操作

    # 会员中心
    url(r'^vip/orders$', vip.viporders, name='vip_orders'),  # 会员中心我的订单
    url(r'^vip/odstate$', vip.odstate, name='vip_odstate'),  # 修改订单状态（确认收货）
    url(r'^vip/info$', vip.info,name='vip_info'), #会员中心的个人信息
    # url(r'^vip/update$', vip.update,name='vip_update'), #执行修改会员信息
    # url(r'^vip/resetps$', vip.resetps,name='vip_resetps'), #重置密码表单
    # url(r'^vip/doresetps$', vip.doresetps,name='vip_doresetps'), #执行重置密码


]
