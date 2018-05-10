from urllib import request,parse
from http import cookiejar

# cookie容器
cookie = cookiejar.CookieJar()
# cookie管理器
cookie_handler = request.HTTPCookieProcessor(cookie)
# 带cookie的请求管理器
opener  = request.build_opener(cookie_handler)

url = ''
data = {}
headers = {}


res = opener.open()
res_data = res.content.decode('utf-8')

