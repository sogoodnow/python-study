from django.conf.urls import url,include
from .views import index

urlpatterns = [
    # 前台首页

    url(r'^$', index.index, name="index"),
    url(r'^detail/(?P<gid>[0-9]+)$', index.detail, name="pdetail"),#商品详情
    url(r'^list$', index.plists, name="list"),
    url(r'^list/(?P<pindex>[0-9]+)$', index.plists, name="list"),

    # 会员登录
    url(r'^login$', index.login, name="login"),
    url(r'^dologin/$', index.dologin, name="dologin"),
    url(r'^logout/$', index.logout, name="logout"),
    url(r'^register/$', index.register, name="register"),
    url(r'^doregister/$', index.doregister, name="doregister"),
]
