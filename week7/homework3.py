import requests,re

# 定义请求参数
s = requests.session()

# 抓取信息
def get_content(pindex):
    '''
    抓取分页信息
    :param pindex: 页码
    :return:
    '''
    url = 'http://bj.58.com/dashanzi/chuzu/pn'+str(pindex)+'/?ClickID=1'
    res = s.get(url).content.decode('utf-8')

    divlist = re.findall('<div class="des">.*|\n</div>',res,re.S)
    print(len(divlist))
    try:
        pass
    except Exception as e:
        pass


# 解析信息


if __name__ == '__main__':
    get_content(1)