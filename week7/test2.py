import urllib3,requests,re

url = "http://www.baidu.com"
# http = urllib3.PoolManager()
# res = http.request('GET',url)
# print(res.status)
# data = res.data.decode("utf-8")
# print(data)

res = requests.get(url)
print(res.status_code)
print(res.encoding)
# res.text
data = res.content.decode("utf-8")
print(re.findall("<title>(.*?)</title>",data))

