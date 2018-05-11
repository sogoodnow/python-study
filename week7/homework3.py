import requests,re,lxml
from bs4 import BeautifulSoup

# 状态维持
s = requests.session()
# 定义存储信息列表
finall_list = []
max_page = 0
# 抓取信息
def get_content(pindex):
    '''
    抓取分页信息
    :param pindex: 页码
    :return:finall_list 结果列表
    '''
    global max_page
    try:
    # 发起请求
        url = 'http://bj.58.com/dashanzi/chuzu/pn'+str(pindex)+'/?ClickID=1'
        res = s.get(url).content.decode('utf-8')
        # print(res)
        # soup定义
        soup = BeautifulSoup(res, "lxml")
        dlist = soup.select('.listUl li')
        # 遍历房源ul标签中里li
        for tag in dlist:
            # 获取最大页数
            if max_page == 0:
                if tag.select(".next"):
                    max_page = int(tag.select(".next")[0].previous)
            # 标题
            if tag.select(".des h2 a"):
                title = tag.select(".des h2 a")[0].get_text()
                title = str(title).strip()
            else:
                title=''
            # 图片
            if tag.select(".img_list a img[lazy_src]"):
                pic = tag.select(".img_list a img[lazy_src]")[0].get('lazy_src')
            else:
                pic = ''
            # 户型
            if tag.select(".des p"):
                roomtype = tag.select(".des p")[0].get_text()
                roomtype = ''.join(re.split(r'\s+', str(roomtype)))
            else:
                roomtype = ''
            # 价格
            if tag.select(".money b"):
                money = tag.select(".money b")[0].get_text() + "元"
            else:
                money = ''
            # 放入字典并添加至结果列表
            dic = {'标题': title, '图片': pic, '房型': roomtype, '价格': money,'页码':pindex}
            finall_list.append(dic)
        # 不为最大页数则递归调用
        if pindex < max_page:
            get_content(int(pindex) + 1)
        elif pindex == max_page:
            # print(len(finall_list))
            return finall_list
    except Exception as e:
        if hasattr(e,"code"):
            print("请求出错")
        else:
            print("其他错误"+str(e))

# 主函数
if __name__ == '__main__':
    get_content(1)
    print("总爬取数："+str(len(finall_list)))
    for i in finall_list:
        if i['标题']:
            print(i)
        else:
            # 移除无效数据
            finall_list.remove(i)
    print("有效数：" + str(len(finall_list)))