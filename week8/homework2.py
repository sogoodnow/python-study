import requests
from lxml import etree

"""
思路：https://item.jd.com/5001209.html，商品页面中商品详情的链接数值，对应的是商品SKU（pid）
模拟添加购物车时，请求地址为：https://cart.jd.com/gate.action?pid=7348367&pcount=1&ptype=1
参数分别为pid，数量，类型（可省略）
"""
# 使用session维持cookie状态
s = requests.session()
# 商品列表
goods = []

# 添加商品至购物车
def add_cart():
    headers = {
        'User-Agent': 'User-Agent:Mozilla/5.0(WindowsNT6.1;rv:2.0.1)Gecko/20100101Firefox/4.0.1',
    }
    # 进入商品详情页面
    pr1_rul = 'https://item.jd.com/7348367.html'
    s.get(pr1_rul,headers=headers)
    pr1_rul = 'https://item.jd.com/5001209.html'
    s.get(pr1_rul,headers=headers)
    # 添加至购物车
    s.get('https://cart.jd.com/gate.action?pid=7348367&pcount=1&ptype=1')
    s.get('https://cart.jd.com/gate.action?pid=5853579&pcount=1&ptype=1')

    # 测试信息----查看cookie信息
    # print({c.name : c.value for c in s.cookies})


# 查看解析购物车内容
def cart_view():
    sku1 = '7348367'
    sku2 = '5853579'
    # 购物车地址
    url_view = 'https://cart.jd.com/cart.action'
    res = s.get(url_view).content.decode('utf-8')
    # 解析购物车商品
    html = etree.HTML(res)
    # 商品1
    goods_name1 = html.xpath('//div[@skuid='+sku1+']//div[@class="p-name"]/a/text()')[0]
    goods_img1 = "https:"+html.xpath('//div[@skuid='+sku1+']//div[@class="p-img"]/a/img/@src')[0]
    goods_price1 = html.xpath('//div[@skuid='+sku1+']//div[@class="cell p-price p-price-new "]/strong/text()')[0]
    dic1 = {"商品名":goods_name1,"商品图片":goods_img1,"商品价格":goods_price1}

    # 商品2
    goods_name2 = html.xpath('//div[@skuid='+sku2+']//div[@class="p-name"]/a/text()')[0]
    goods_img2 = "https:"+html.xpath('//div[@skuid='+sku2+']//div[@class="p-img"]/a/img/@src')[0]
    goods_price2 = html.xpath('//div[@skuid='+sku2+']//div[@class="cell p-price p-price-new "]/strong/text()')[0]
    dic2 = {"商品名":goods_name2,"商品图片":goods_img2,"商品价格":goods_price2}

    #添加至列表
    goods.append(dic1)
    goods.append(dic2)

# 主函数
if __name__ == '__main__':
    add_cart()
    cart_view()
    # 输出商品
    for item in goods:
        for k ,v in item.items():
            print(k+":"+str(v).strip()+'\n')
        print("*"*50)