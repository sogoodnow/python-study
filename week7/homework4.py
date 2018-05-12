import requests,re,lxml
from bs4 import BeautifulSoup

s = requests.session()
res_list=[]
def get_data(pidnex):
    url = 'http://maoyan.com/board/4?offset='+str(pidnex)
    headers = {
        'User-Agent': 'User-Agent:Mozilla/5.0(WindowsNT6.1;rv:2.0.1)Gecko/20100101Firefox/4.0.1'
    }
    try:
        res = s.get(url,headers=headers).content.decode('utf-8')
        soup = BeautifulSoup(res,'lxml')
        # 找到对应列表
        dilist = soup.select(".board-wrapper dd ")
        # 遍历信息
        for i in dilist:
            # 存放字典
            dic = {}

            # 文字类信息
            mes = i.text.strip('\n').split()
            if mes[0]:
                dic["排名"] = mes[0]
            else:
                dic["排名"] = ""
            if mes[1]:
                dic["片名"] = mes[1]
            else:
                dic["片名"] = ""
            if mes[2]:
                dic["主演"] = mes[2]
            else:
                dic["主演"] = ""
            if mes[3]:
                dic["上映时间"] = mes[3]
            else:
                dic["上映时间"] = ""
            if mes[4]:
                dic["得分"] = mes[4]
            else:
                dic["得分"] = ""
            res_list.append(dic)
            # 图片路径
            if i.select(".board-img"):
                dic["图片"] = i.select(".board-img")[0].get('data-src')
            else:
                dic["图片"] = ""
        if int(pidnex) == 90:
            return res_list
        else:
           get_data(int(pidnex)+10)
    except Exception as e:
        if hasattr(e,'code'):
            print("请求访问出错")
        else:
            print("其他错误"+str(e.reason))


if __name__ == '__main__':
    get_data(0)
    # for item in res_list:
    #     print(item)
    with open("./movie.txt",'w',encoding='utf-8') as f:
        for line in res_list:
            f.writelines(str(line)+'\n')
