from django.conf.urls import url,include
from web.views import index

urlpatterns = [

    # web首页
    url(r'^$',index.index ,name="index"),

]
