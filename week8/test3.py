import requests
import re
import os

url = r'http://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1526828856935_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&hs=2&ctd=1526828856935%5E00_3423X198&word=%E7%BE%8E%E8%85%BF%E4%BC%98%E7%BE%8E%E6%97%97%E8%A2%8D%E7%BE%8E%E5%A5%B3'
dirpath = r'F:\img'

html = requests.get(url).text
urls = re.findall(r'"objURL":"(.*?)"', html)

if not os.path.isdir(dirpath):
    os.mkdir(dirpath)

index = 1
for url in urls:
    print("Downloading:", url)
    try:
        res = requests.get(url)
        if str(res.status_code)[0] == "4":
            print("未下载成功：", url)
            continue
    except Exception as e:
        print("未下载成功：", url)
    filename = os.path.join(dirpath, str(index) + ".jpg")
    with open(filename, 'wb') as f:
        f.write(res.content)
        index += 1

print("下载结束，一共 %s 张图片" % index)