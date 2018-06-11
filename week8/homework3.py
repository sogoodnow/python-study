import time,random,requests,json,os,re,gzip
from urllib.request import urlretrieve
from urllib.parse import urlencode,unquote

# 状态维持
s = requests.session()
# 图片名称列表
ls_img = []
# 伪造时间参数
pra_time = str(time.time())[0:8] + str(random.randint(10000, 20000))
# 用于存储所有的图片地址，用于添加时判断是否链接已存在
img_url = []
# 存放获取失败时，所创建的文件夹名称
err_path = []

# 模拟点击街拍分类
def getpage(page,keyword):
    # 请求参数
    params = {
        'tn': 'resultjson_com',
        'ipn': 'rj',
        'ct': '201326592',
        'cl': '2',
        'lm': '-1',
        'ie': 'utf - 8',
        'oe': 'utf - 8',
        'st':'-1',
        'ic': '0',
        'fp': 'result',
        'queryWord': keyword,
        'word': keyword,
        'pn':page,
        'rn':'30',
        'face': '0',
        'istype': '2',
        'nc': '1',
        'gsm': '3c',
        pra_time:'',
    }
    # 抓取地址
    try:
        # 下拉后ajax显示图片
        url2 = 'http://image.baidu.com/search/acjson?'+urlencode(params)
        res2 = s.get(url2)
        return json.loads(res2.content.decode('utf-8'))
    except requests.ConnectionError:
        return None

def getimage(aj_json):
   # 是否有data
   if aj_json.get('data'):
        # 遍历data，获取标题及文件名
        for i in aj_json.get('data'):
            if i.get('fromPageTitleEnc') and i.get('objURL'):
                # 解码链接
                objURL = str(baidtu_uncomplie(i.get('objURL')))
                # 去除非图片后缀结尾的链接
                if objURL.split('.').pop() not in 'jpg,jpeg':
                    continue
                print(objURL)
                # 判断是否有相同重复链接，如果有则跳过
                if objURL in img_url:
                    continue
                # 如果没有则添加字典和列表
                else:
                    img_url.append(objURL)
                    ls_img.append({"title":i.get('fromPageTitleEnc'),"filename":objURL})

# 百度图片地址解码函数
def  baidtu_uncomplie(zurl):
    res = ''
    # 链接头
    c = ['_z2C$q', '_z&e3B', 'AzdH3F']
    # 解码字典
    d= {'w':'a', 'k':'b', 'v':'c', '1':'d', 'j':'e', 'u':'f', '2':'g', 'i':'h',
        't':'i', '3':'j', 'h':'k', 's':'l', '4':'m', 'g':'n', '5':'o', 'r':'p',
        'q':'q', '6':'r', 'f':'s', 'p':'t', '7':'u', 'e':'v', 'o':'w', '8':'1',
        'd':'2', 'n':'3', '9':'4', 'c':'5', 'm':'6', '0':'7', 'b':'8', 'l':'9',
        'a':'0', '_z2C$q':':', '_z&e3B':'.', 'AzdH3F':'/'}
    if((zurl == None) or ('http' in zurl)):
        return zurl
    else:
        j= zurl
        for m in c:
            j=j.replace(m,d[m])
        for char in j:
            if re.match('^[a-w\d]+$',char):
                char = d[char]
            res= res+char
        return res

# 图片保存
def saveimg():
    # 遍历图片列表
    global img_count
    for img in ls_img:
        # 获取文件标题
        title = img.get('title')
        # 图片地址
        file_url = img.get('filename')
        # print(file_url)
        # 处理每组图片的存储路径
        cp = str(title).strip().split()[0]
        cp = re.split('[\W]',cp)
        # 没有文件标题的情况下，归类到【其他文件夹】
        if cp[0]:
            path = os.path.join("./mypic/", cp[0])
        else:
            path = os.path.join("./mypic/",'其他')
        # 文件夹不存在则创建
        if not os.path.exists(path):
            os.makedirs(path)
        try:
            img_path = path+'/'+str(time.time())+'.jpg'
            print(img_path)
            # urlretrieve(file_url,path)
            # 设置超时参数0.1
            with s.get(file_url, stream=True,timeout=1) as ir:  # 使用with的好处不用考虑close关闭问题。
                with open(img_path, 'wb') as f:
                    for chunk in ir:
                        f.write(chunk)
            img_count += 1
        except Exception as e:
            # 清理无数据文件夹
            if os.path.exists(path) and len(os.listdir(path)) == 0:
                try:
                    os.removedirs(path)
                except IOError as ioe:
                    print(str(ioe))
            print(str(e))
            pass


if __name__ == '__main__':
    # 图片爬取成功总数
    global img_count
    img_count = 0
    while True:
        keyword = input("输入图片关键字：")
        page = input('请输入抓取页数：')
        if re.match('\W',keyword):
            print('请输入有效文字！')
            continue
        if re.match('[^\d]',page):
            print('请输入有效文字！')
            continue
        start_time = time.time()
        # 请求头信息
        headers = {
            'User-Agent': 'User-Agent:Mozilla/5.0(WindowsNT6.1;rv:2.0.1)Gecko/20100101Firefox/4.0.1',
        }
        params = {
            'tn': 'baiduimage',
            'ipn': 'r',
            'ct': '201326592',
            'cl': '2',
            'lm': '-1',
            'st': '-1',
            'fm': 'result',
            'sf': '1',
            'fmq': '1526877991010_R',
            'ic': '0',
            'nc': '1',
            'se': '1',
            'showtab': '0',
            'fb': '0',
            'face': '0',
            'istype': '2',
            'ie': 'utf - 8',
            'ctd': '1526877991010 ^ 00_1903X577',
            'word': keyword
    }
        # 地址
        url1 = "https://image.baidu.com/search/index?" + urlencode(params)
        s.get(url1,headers=headers)
        # 每隔0.5秒爬30张图片，添加至列表，保存至本地
        for i in range(0,int(page)*30,30):
            res_json = getpage(i,keyword)
            getimage(res_json)
            saveimg()
            time.sleep(0.5)
        end_time = time.time()
        # 信息打印
        print('*' * 50)
        print("成功爬取图片总数：" + str(img_count)+',抓取耗时：'+str(round(end_time-start_time,2))+'秒')
        print('*'*50)

