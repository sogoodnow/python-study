import requests

s = requests.session()

# 添加商品至购物车
def add_cart():
    headers = {
        'User-Agent': 'User-Agent:Mozilla/5.0(WindowsNT6.1;rv:2.0.1)Gecko/20100101Firefox/4.0.1',
    }

    url_add = 'https://cart.jd.com/addToCart.html?rcd=1&pid=6946605&pc=1&eb=1&rid=1526628918519&em= '
    res_add = s.get(url_add, headers=headers)
    print(res_add.content.decode('utf-8'))


# 查看解析购物车内容
def cart_view():
    url_view = 'https://cart.jd.com/cart.action'
    res = s.get(url_view,headers=headers).text
    print(res)


# 主函数
if __name__ == '__main__':
    add_cart()
    # cart_view()