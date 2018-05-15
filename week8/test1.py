import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve

# 定义请求url地址
url = "https://list.jd.com/list.html?cat=9987,653,655"

# 使用requests爬取指定url信息
res = requests.get(url)
#print(res.text)

# 使用BeautifulSoup创建解析器
soup = BeautifulSoup(res.text,"lxml")

# 解析里面的所有商品图片
imlist = soup.find_all(name="img",attrs={"width":"220","height":"220"})
#print(len(imlist))

# 遍历并解析里面的图片url地址信息
m=1
for im in imlist:
    #首先判断有无src属性来决定如何获取
    if 'src' in im.attrs:
        imurl = "https:"+im.attrs['src']
    else:
        imurl = "https:"+im.attrs['data-lazy-img']

    #储存图片（两种方式）
    # 使用urllib中urlretrieve直接存储图片
    urlretrieve(imurl,'./mypic/p'+str(m)+'.jpg')
    '''
    # 默认情况下，当您发出请求时，响应正文会立即下载，而设置stream参数为true，则只有响应头已经下载并且连接保持打开状态。
    with requests.get(imurl, stream=True) as ir: # 使用with的好处不用考虑close关闭问题。
        with open('./mypic/p'+str(m)+'.jpg', 'wb') as f:
            for chunk in ir:
                f.write(chunk)
    '''           
    print('p'+str(m)+'.jpg')
    m += 1