import urllib,requests,json,gzip
from urllib import request,parse
def tanslate(keywords):
    '''urllib有道文字翻译'''
    # 请求地址
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    # 请求数据
    data = {
        'action': 'FY_BY_CLICKBUTTION',
        'client': 'fanyideskweb',
        'doctype': 'json',
        'from': 'AUTO',
        'i': keywords,
        'keyfrom': 'fanyi.web',
        'salt': '1525781061437',
        'sign': '12b76773ee9320e0a11f6193ee99c871',
        'smartresult': 'dict',
        'to': 'AUTO',
        'typoResult': 'false',
        'version': '2.1'
    }
    # 编码
    data = parse.urlencode(data)
    # 头信息
    headers = {
        'Content-Length': len(data)
    }
    # 发起请求
    try:
        req = request.Request(url=url,data=bytes(data,encoding='utf-8'),headers=headers)
        res = request.urlopen(req)
        res_json = res.read().decode('utf-8')
        dic = json.loads(res_json)
        print('=' * 3 + dic['translateResult'][0][0]['tgt'])
    except Exception as e:
        if hasattr(e,'code'):
            print("访问地址出错")
        else:
            print("其他错误"+str(e))



if __name__ == '__main__':
    while True:
        keywords = input("请输入要翻译的文字：\n")
        if keywords != "q":
            tanslate(keywords)
        else:
            break