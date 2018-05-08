import requests,json

def tanslate(keywords):
    '''requests有道文字翻译'''
    # 请求地址
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    # 请求数据
    data = {
        'i': keywords,
        ' from':'AUTO',
        'to':'AUTO'	,
        'smartre sult':'dict',
        'client':'faskweb',
        'salt':'15247642',
        'sign':'6a0f9456d45f7ac209fe9ff2e60d1f',
        'doctype':'json','version':'2.1' ,
        'keyfrom':'fanyi.web',
        'action':'FY_BY_REALTIME',
         'typoResult':'false'
    }
    # 发起请求
    try:
        res = requests.post(url,data=data)

        print(res.content.decode('utf-8'))
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