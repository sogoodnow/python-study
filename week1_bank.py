# 实现一个自动取款机的存取款模拟效果。
# 要求有登陆和退出、查询余额、取钱，存钱等操作
# 学员姓名：邱国昌
# 日期：2018-03-15

def menu_print():
    """
    用于打印登录窗体
    :return:
    """
    Line = "="
    print(Line*16, "欢迎进入黄金银行", Line*20)
    print("|   {:<16}  |    {:<16}  |".format("1.用户登录", "2.余额查询"))
    print("|   {:<18}  |    {:<18}  |".format("3.取款", "4.存款"))
    print(Line*54)

def user_db():
    # 随机生成用户列表，包含用户卡号、密码、用户姓名、用户余额、编码
    users = [
             {"姓名": "张三", "卡号": "100001", "密码": "123456", "编码": "0001", "余额": "98654"},
             {"姓名": "李四", "卡号": "100002", "密码": "123456", "编码": "0002", "余额": "235"},
             {"姓名": "赵五", "卡号": "100003", "密码": "123456", "编码": "0003", "余额": "1235"},
             {"姓名": "孙六", "卡号": "100004", "密码": "123456", "编码": "0004", "余额": "3545"},
             {"姓名": "王七", "卡号": "100005", "密码": "123456", "编码": "0005", "余额": "18"}
             ]


while True:
    # 生成后台数据
    user_db()
    # 打印窗口界面
    menu_print()
    break
    # 存取操作，1.余额查询 2.取款 3.存款

