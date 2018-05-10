import re,os

with open('./test.html','r',encoding='UTF-8') as f:
    data = f.read()
    pat = '<a href=\"http://jxjump.58.com/service\?target=(.*?)\" tongji_label=\"listclick\"  onclick=\"clickLog(\'from=fcpc_zflist_gzcount\');\" target=\"_blank\"  rel=\"nofollow\" >(.*?)</a>'

    dlist = re.findall(pat,data)

    print(dlist)