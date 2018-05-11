import requests,re,lxml
from bs4 import BeautifulSoup

s = requests.session()
def get_data(pidnex):

    url = 'http://maoyan.com/board/4?offset='+str(pidnex)
    headers = {
        'User-Agent': 'User-Agent:Mozilla/5.0(WindowsNT6.1;rv:2.0.1)Gecko/20100101Firefox/4.0.1'
    }
    try:
        res = s.get(url,headers=headers).content.decode('utf-8')
        soup = BeautifulSoup(res,'lxml')
        print(soup.select(".board-wrapper dd "))
    except Exception as e:
        if hasattr(e,'code'):
            print("请求访问出错")
        else:
            print("其他错误"+str(e.reason))


if __name__ == '__main__':
    get_data(0)