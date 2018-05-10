import requests,re,urllib,json

def tanslate(keyword):
    # 定义请求参数
    url = 'http://fanyi.baidu.com/sug'
    data = {'kw':keyword}
    # 发起请求，接受response
    res = requests.post(url,data)
    res_json = res.content.decode('utf-8')
    # 转换json
    res_json = json.loads(res_json)
    # 输出
    print(res_json['data'][0]['v'])



if __name__ == '__main__':
    while True:
        keyword = input("请输入要翻译的值\n")
        if keyword == 'q':
            break
        else:
            tanslate(keyword)
