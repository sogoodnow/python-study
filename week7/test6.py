import re,os,lxml
from bs4 import BeautifulSoup
with open('./test.html','r',encoding='UTF-8') as f:
    data = f.read()

    soup = BeautifulSoup(data,"lxml")
    dlist = soup.select('.listUl li')
    for tag in dlist:
        # 标题
        title = tag.select(".des h2 a")[0].get_text()
        print(title)
        # 图片
        pic = tag.select(".img_list a img[lazy_src]")[0].get('lazy_src')
        print(pic)
        # 户型
        roomtype = tag.select(".des p")[0].get_text()
        roomtype = ''.join(re.split(r'\s+',str(roomtype)))
        print(roomtype)
        # 价格
        money = tag.select(".money b")[0].get_text()+"元"
        print(money)
        dic = {'title':title,'pic':pic,'roomtype':roomtype,'money':money}

