import re


str = 'asdfasdf2018-0dfadf6-03dfadfa'
res = re.findall('\d{4}',str)
print(res[0])