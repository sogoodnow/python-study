from django.conf.urls import url,include
from .views import index

urlpatterns = [
    # 前台首页
    url(r'^$', index.index, name="index"),    #商城首页
    url(r'^list$',index.plists, name = "plist"),
    url(r'^detail/(?P<gid>[0-9]+)$', index.detail, name="pdetail"),#商品详情

]
