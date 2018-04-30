from django.conf.urls import url,include
from .views import index,users,types,goods

urlpatterns = [

    # 后台登录
    url(r'^$',index.index ,name="myadmin_index"),
    url(r'^verify$',index.verify ,name="myadmin_verify"),
    url(r'^login$',index.login ,name="myadmin_login"),
    url(r'^dologin$',index.dologin ,name="myadmin_dologin"),
    url(r'^logout$',index.logout ,name="myadmin_logout"),
    # 用户管理
    url(r'^users/(?P<pIndex>[0-9]+)$',users.index ,name="myadmin_users_index"),
    url(r'^search/(?P<pIndex>[0-9]+)$',users.search ,name="myadmin_users_search"),
    url(r'^users/add$',users.add ,name="myadmin_users_add"),
    url(r'^users/insert$',users.insert ,name="myadmin_users_insert"),
    url(r'^users/del/(?P<uid>[0-9]+)$',users.delete ,name="myadmin_users_del"),
    url(r'^users/edit/(?P<uid>[0-9]+)$',users.edit ,name="myadmin_users_edit"),
    url(r'^users/update/(?P<uid>[0-9]+)$',users.update ,name="myadmin_users_update"),
    url(r'^users/restpwd/(?P<uid>[0-9]+)$',users.restpwd ,name="myadmin_users_restpwd"),
    url(r'^users/pwdupdate/(?P<uid>[0-9]+)$',users.pwdupdate ,name="myadmin_users_pwdupdate"),
    # 商品类别管理
    url(r'^types/$', types.index, name="myadmin_types_index"),
    url(r'^types/add(?P<tid>[0-9]+)$', types.add, name="myadmin_types_add"),
    url(r'^types/insert$', types.insert, name="myadmin_types_insert"),
    url(r'^types/del/(?P<tid>[0-9]+)$', types.delete, name="myadmin_types_del"),
    url(r'^types/edit/(?P<tid>[0-9]+)$', types.edit, name="myadmin_types_edit"),
    url(r'^types/update/(?P<tid>[0-9]+)$', types.update, name="myadmin_types_update"),

    # 商品信息管理
    url(r'^goods/$', goods.index, name="myadmin_goods_index"),
    url(r'^goods/add/$', goods.add, name="myadmin_goods_add"),
    url(r'^goods/insert$', goods.insert, name="myadmin_goods_insert"),
    url(r'^goods/del/(?P<gid>[0-9]+)$', goods.delete, name="myadmin_goods_del"),
    url(r'^goods/edit/(?P<gid>[0-9]+)$', goods.edit, name="myadmin_goods_edit"),
    url(r'^goods/update/(?P<gid>[0-9]+)$', goods.update, name="myadmin_goods_update"),
    url(r'^goods/ueditor$', goods.ueditor, name="myadmin_goods_ueditor"),


]
