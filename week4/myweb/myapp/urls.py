"""myweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from . import views
from django.conf.urls import url
from django.contrib import admin


urlpatterns = [
    url(r'^$', views.index,name="index"),
    url(r'^main/$', views.usermain,name="main"),
    url(r'^main/(?P<pIndex>[0-9]+)$', views.usermain,name="main"),
    url(r'^stuedit/$', views.stuedit,name="stuedit"),
    url(r'^stuedit/(?P<uid>[0-9]+)$', views.stuedit,name="stuedit"),
    url(r'^stuadd/', views.stuadd,name="stuadd"),
    url(r'^picupload/$', views.picupload,name="picupload"),
    url(r'^picupload/(?P<uid>[0-9]+)$', views.picupload,name="picupload"),
    url(r'^studel/(?P<uid>[0-9]+)$', views.studel,name="studel"),
    url(r'^savefile/(?P<uid>[0-9]+)$', views.savefile, name="savefile"),

]
