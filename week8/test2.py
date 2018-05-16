import requests,re

url ='https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv1122&productId=12144506757&score=0&sortType=5&page=1&pageSize=10&isShadowSku=0&rid=0&fold=1'
res = requests.get(url).text

pat ='"content":"(.*?)"'
print(re.findall(pat,res,re.S))