from  urllib import request,parse
from http import cookiejar
import requests

cookie = cookiejar.CookieJar()
handler = request.HTTPCookieProcessor(cookie)
opener = request.build_opener(handler)

login_url = 'http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=2018412120762'
data = {

'captcha_type':'web_login ',
'domain	':'renren.com',
'email':'13951502395',
'f	':' http%3A%2F%2Fzhibo.renren.com%2Ftop',
'icode	':'',
'key_id	':'1',
'origURL':'http://www.renren.com/home',
'password':'50ae34925480547f5c56dab168723f4571600bcab37fbd36a8c33b10bf08b7ed',
'rkey'	:'2a442cd0c2f740407d5480c939cb9b50'
}
data = parse.urlencode(data)
headers = {
    'Content-Length':len(data)
}

req = request.Request(login_url,data=bytes(data,encoding='utf-8'),headers=headers)
res = request.urlopen(req)

print(res.read().decode('utf-8'))