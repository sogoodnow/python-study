# 实现一个自动取款机的存取款模拟效果。
# 要求有登陆和退出、查询余额、取钱，存钱等操作
# 学员姓名：邱国昌
# 日期：2018-03-15


hasLogin = False  # 全局变量判断用户是否已经登录过，输入过密码
user_info = {}    # 存储单个用户字典
# 随机生成用户列表，包含用户卡号、密码、用户姓名、用户余额、编码
users = [
         {"姓名": "张三", "卡号": "100001", "密码": "123456", "编码": "0001", "余额": "9854"},
         {"姓名": "李四", "卡号": "100002", "密码": "123456", "编码": "0002", "余额": "235"},
         {"姓名": "赵五", "卡号": "100003", "密码": "123456", "编码": "0003", "余额": "1235"},
         {"姓名": "孙六", "卡号": "100004", "密码": "123456", "编码": "0004", "余额": "3545"},
         {"姓名": "王七", "卡号": "100005", "密码": "123456", "编码": "0005", "余额": "18"}
         ]


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

def menu_welcome(user_name):
    """
    用于打印登陆成功后界面，由用户【1登录变为】 【1退出登录】
    :user_name: 传入用户姓名
    :return:
    """
    Line = "="
    if not hasLogin:
        print("登录成功！")
    else:
        print(Line*16, "欢迎您，尊敬的"+user_name+"先生", Line*14)
        print("|   {:<16}  |    {:<16}  |".format("1.退出登录", "2.余额查询"))
        print("|   {:<18}  |    {:<18}  |".format("3.取款", "4.存款"))
        print(Line*54)

def bank_ops(op_no):
    """
    用于用户登录后的操作
    :param op_no:
    :return:
    """
    global hasLogin   # 初始值为未登录，0
    global user_info  # 单用户信息
    if op_no == "1":  # 退出登录
        print("感谢您的使用，请确认已退卡，欢迎您下次光临！")
        hasLogin = False  # 设置登录标记为退出（未登录）
    if op_no == "2":  # 余额查询
        print("您当前的余额为：{}元".format(str(user_info['余额'])))
        hasLogin = True
        return
    if op_no == "3":  # 取款操作
        out = int(input("请您输入取款金额："))   # 用户输入取款金额
        while out > int(user_info["余额"]):      # 取款金额大于余额时报错，并要求重新输入
            out = int(input("超出余额，请重新输入："))
        else:
            new_count = int(user_info["余额"]) - out   # 正常取款时，余额计算
            user_info["余额"] = str(new_count)         # 更新用户字典，保证再次查询时余额显示
            print("完成！您的当前余额为：", str(new_count)+"元")   # 打印成功凭证
    if op_no == "4":  # 存款操作
        store = int(input("请您输入存款金额："))   # 用户存款金额
        while 0 >= int(user_info["余额"]):      # 取款金额大于余额时报错，并要求重新输入
            store = int(input("请输入正数金额："))
        else:
            new_count = int(user_info["余额"]) + store   # 正常存款时，余额计算
            user_info["余额"] = str(new_count)         # 更新用户字典，保证再次查询时余额显示(再次登录时余额未做）
            print("完成！您的当前余额为：", str(new_count)+"元")   # 打印成功凭证

def user_login(op_no):
    """
    #用于用户登录操作
    :param op_no: 传入的操作编号
    :return:返回单个用户
    """
    global hasLogin  # 初始值为未登录，0
    global user_info  # 用户信息

    # 如果用户未登录而且选择登录以外其他业务时，报出信息并要求用户进行登录
    if not hasLogin and op_no != "1":
        print("请您先登录您的账户")
        ag_no = input("请输入您的业务：")  # 重新输入后递归调用
        user_login(ag_no)
        return user_info
    # 如果用户进行登录，则判断是否有用户，若存在用户则保留用户信息，不存在则提示信息并请求其重新登录
    elif op_no == "1":
        # 接收用户输入的卡号和密码
        card_no = input("请您输入卡号：")
        pass_wd = input("请您输入密码:")

        """
        处理逻辑说明：判断卡号是否存在及密码是否有误，有误则要求重新输入卡号密码
        变量i 用于计算遍历时的次数，先进行用户及密码匹配，如果所有用户都遍历了，
        但仍然没有匹配到，暨i次数已经到达列表长度时，则结束，并要求用户重新输入
        """
        i = 0
        for user in users:  # 遍历用户信息表，每次循环代表一个用户
            i += 1
            cn = len(users)
            if user["卡号"] == card_no and user["密码"] == pass_wd:  # 如果有卡号信息，则进一步判断用户的密码是否正确
                hasLogin = True  # 如果登陆成功，则把登陆标识符设置为1
                user_info = user   # 如果匹配到用户则返回用户信息
                return user
            elif i == cn:  # 如果遍历用户列表没有找到相关信息，则返回错误信息，
                print("用户信息有误，请重新输入")
                ag_no = input("请输入您的业务：")  # 重新输入后递归调用
                user_login(ag_no)  # 递归调用函数
    return user_info

while True:
    opNo = 0  # 操作参数
    # 判断是否已经登录，hasLogin初始值为FALSE
    if hasLogin:
        menu_welcome(user_info['姓名'])   # 已经登录的用户显示已登录界面
        opNo = input("请输入您的业务：")  # 接收用户操作参数
        bank_ops(opNo)         # 调用银行操作方法
    else:
        # 初始化用户列表信息，users为全局变量
        menu_print()   # 初次进入界面，或者退出登录以后，显示欢迎登录界面
        opNo = input("请输入您的业务：")  # 接收用户操作参数
        user_info = user_login(opNo)      # 执行用户登录，如果登录成功则返回该用户信息



