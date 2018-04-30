from django.conf.urls import url,include
from .views import index

urlpatterns = [
    # 前台首页
    url(r'^list$',index.plists,name="cp"),
    url(r'^$', index.index, name="index"),
    url(r'^detail/(?P<gid>[0-9]+)$', index.detail, name="pdetail"),#商品详情
]
