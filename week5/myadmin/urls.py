from django.conf.urls import url,include
from myadmin.views import index

urlpatterns = [
    # 后台首页
    url(r'^$',index.index ,name="myadmin_index"),

]
