from django.conf.urls import url,include
from .views import index,users

urlpatterns = [
    # 后台首页
    url(r'^$',index.index ,name="myadmin_index"),
    url(r'^users$',users.index ,name="myadmin_users_index"),
    url(r'^users/add$',users.add ,name="myadmin_users_add"),
    url(r'^users/insert$',users.insert ,name="myadmin_users_insert"),
    url(r'^users/del/(?P<uid>[0-9]+)$',users.delete ,name="myadmin_users_del"),
    url(r'^users/edit/(?P<uid>[0-9]+)$',users.edit ,name="myadmin_users_edit"),
    url(r'^users/update/(?P<uid>[0-9]+)$',users.update ,name="myadmin_users_update"),

]
