import time,random,requests,json,os,re,gzip
from urllib.request import urlretrieve
from urllib.parse import urlencode

# 状态维持
s = requests.session()
# 图片名称列表
ls_img = []
# 伪造时间参数
pra_time = str(time.time())[0:8] + str(random.randint(10000, 20000))

# 模拟点击街拍分类


def getpage(page):
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
        'queryWord': '美腿优美旗袍美女',
        'word': '美腿优美旗袍美女',
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
        # print(res2.content.decode('utf-8'))
        return json.loads(res2.content.decode('utf-8'))
    except requests.ConnectionError:
        return None

def getimage(res_json):
   # 是否有data
   if res_json.get('data'):
        # 遍历data，获取标题及文件名
        for i in res_json.get('data'):
            if i.get('fromPageTitleEnc') and i.get('objURL'):
                # 添加至图片列表
                print(i.get('ObjURL'))
                ls_img.append({"title":i.get('fromPageTitleEnc'),"filename":i.get('objURL')})

def saveimg():
    # 遍历图片列表
    for img in ls_img:
        # 获取文件标题
        title = img.get('title')
        # 图片地址
        file_url = img.get('filename')
        # print(file_url)
        # 处理每组图片的存储路径
        cp = str(title).split()[0]
        cp = re.split('[\W]',cp)
        path = os.path.join("./mypic/", cp[0])
        if not os.path.exists(path):
            os.makedirs(path)
        try:
            img_path = path+'/'+str(time.time())+'.jpg'
            print(img_path)
            urlretrieve(file_url,img_path)
            # print(file_url)
            # with requests.get(file_url, stream=True) as ir:  # 使用with的好处不用考虑close关闭问题。
            #     with gzip.open(img_path, 'wb') as f:
            #         for chunk in ir:
            #             f.write(chunk)
        except Exception as e:
            print(str(e))
            pass

if __name__ == '__main__':
    # 进入百度街拍
    headers = {
        'User-Agent': 'User-Agent:Mozilla/5.0(WindowsNT6.1;rv:2.0.1)Gecko/20100101Firefox/4.0.1',
    }
    url1 = "https://image.baidu.com/user/logininfo?src=pc&page=searchresult&time=" + pra_time
    s.get(url1,headers=headers)
    # 每隔0.5秒爬30张图片，添加至列表，保存至本地
    for i in range(0,150,30):
        res_json = getpage(i)
        getimage(res_json)
        saveimg()
        time.sleep(0.5)

