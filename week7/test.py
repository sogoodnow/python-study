from urllib import request,error
import re

url = "http://www.baidu.com"

user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
headers={"User-Agent":user_agent}
req = request.Request(url,headers=headers)

try:
    res = request.urlopen(req)
    html = res.read().decode("utf-8")
    content = re.findall("<title>(.*?)</title>",html)
    print(content)
except Exception as e:
    if hasattr(e,"code"):
        print('http error')



