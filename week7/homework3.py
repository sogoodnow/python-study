import requests,re,lxml
from bs4 import BeautifulSoup

# 状态维持
s = requests.session()
# 抓取信息
def get_content(pindex):
    '''
    抓取分页信息
    :param pindex: 页码
    :return:finall_list 结果列表
    '''
    try:
        # 发起请求
        url = 'http://bj.58.com/dashanzi/chuzu/pn'+str(pindex)+'/?ClickID=1'
        res = s.get(url).content.decode('utf-8')
        # 定义存储信息列表
        finall_list = []
        # soup定义
        soup = BeautifulSoup(res, "lxml")
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
            roomtype = ''.join(re.split(r'\s+', str(roomtype)))
            print(roomtype)
            # 价格
            money = tag.select(".money b")[0].get_text() + "元"
            print(money)
            dic = {'title': title, 'pic': pic, 'roomtype': roomtype, 'money': money}
            finall_list.append(dic)
        return finall_list
    except Exception as e:
        if hasattr(e,"code"):
            print("请求出错")
        else:
            print("其他错误"+str(e))

# 主函数
if __name__ == '__main__':
    get_content(1)