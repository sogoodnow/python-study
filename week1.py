"""
Python学习第一周作业
本周共计3个作业：
1) 使用while和for…in两个循环分别输出四种九九乘法表效果（共计8个）。
2) 使用文件和目录操作，定义一个统计指定目录大小的函数（注意目录中还有子目录）。
3) 参考1.10的综合案例中的学生信息管理，来实现一个自动取款机的存取款模拟效果。
要求有登陆和退出、查询余额、取钱，存钱等操作。
"""
# 学员姓名：邱国昌
# 日期：2018-03-15
# 根据提示输入作业编号

# 用于控制行间隔
LINE_SPACE = 25

'''
1.九九乘法表
'''
def work1():
    # ========for in 左上三角=========
    print("===="*LINE_SPACE+"\n")
    print("for in左上三角" + "\n")
    # 生成10行
    for i in range(1, 10):
        # 生成列
        for j in range(1, i+1):
            # 格式化输出
            print("{}×{}={}".format(j, i, i*j), end="  ")
        # 换行
        print("\n")

    # ========for in 左下三角=========
    print("===="*LINE_SPACE+"\n")
    print("for in左下三角" + "\n")
    # 生成10行
    for i in range(9, 0, -1):
        # 生成列
        for j in range(1, i+1):
            # 格式化输出
            print("{}×{}={}".format(j, i, i*j), end="  ")
        # 换行
        print("\n")

    # ========for in 右上三角=========
    print("===="*LINE_SPACE+"\n")
    print("for in右上三角" + "\n")
    # 生成10行
    for i in range(1, 10):
        # 生成格式空格
        for k in range(1, 10-i):
            print(end="         ")  # 打印算式间的空格
        # 生成列
        for j in range(1, i+1):
            # 格式化输出
            print("{}×{}={:2}".format(j, i, i*j), end="  ")
        # 换行
        print("\n")

    # ========for in 右下三角=========
    print("===="*LINE_SPACE+"\n")
    print("for in右下三角" + "\n")
    # 生成10行
    for i in range(9, 0, -1):
        # 生成格式空格
        for k in range(1, 10-i):
            print(end="         ")  # 打印算式间的空格
        # 生成列
        for j in range(1, i+1):
            # 格式化输出
            print("{}×{}={:2}".format(j, i, i*j), end="  ")
        # 换行
        print("\n")

    # ========while 左上三角=========
    print("===="*LINE_SPACE+"\n")
    print("while 左上三角" + "\n")
    while i < 10:  # 从1到9遍历
        j = 1  # 每次进入循环时把j重置为1
        while j < i+1:  # 每行行数i 乘以 列 j，行数和列数是相等的，例如9行9列，5行5列
            print("{}×{}={:2}".format(j, i, i*j), end=" ")
            j += 1
        print("")
        i += 1

    # ========while 左下三角=========
    print("===="*LINE_SPACE+"\n")
    print("while 左下三角" + "\n")
    i = 9  # 注意，此处i值由改变
    while (i < 10) and (i > 0):
        j = 1
        while j < i+1:
            print("{}×{}={:2}".format(j, i, i*j), end=" ")
            j += 1
        print("")
        i -= 1

    # ========while 右上三角=========
    print("===="*LINE_SPACE+"\n")
    print("while 右上三角" + "\n")
    while i < 10:
        m = 1  # 初始m为1
        '''while 与 for in有区别， for in 中的临时变量定义后为函数局部变量，函数域内可用，并且值会改变
           while 中的变量需要显示定义 ，如此处的 while m ，需在使用前定义m=1
        '''
        while m < 10-i:
            print(end="        ")  # 打印算式间的空格
            m += 1
        j = 1
        while j < i+1:
            print("{}×{}={:2}".format(j, i, i*j), end=" ")
            j += 1
        print("")
        i += 1

    # ========while 右下三角=========
    print("===="*LINE_SPACE+"\n")
    print("while 右下三角" + "\n")
    i = 9  # 第一行打印乘数为9的行
    while (i < 10) and (i > 0):  # 从9 开始遍历，每次减去1
        m = 1  # 初始m为1，空格控制变量，初始值为1 ，表示打印一个单位的空格
        while m < 10-i:  # 需打印的空格数为，10减去当前乘数
            print(end="        ")  # 打印算式间的空格
            m += 1
        j = 1
        while j < i+1:
            print("{}×{}={:2}".format(j, i, i*j), end=" ")
            j += 1
        print("")
        i -= 1
    return 1  # 函数正常结束后，返回1

'''
2.文件处理
'''
def work2():
    print("bbb")


def work3():
    print("ccc")


'''用于主函数执行后输出的共通信息
return ：返回值为接收到的终端录入命令
'''
def commonprint():
    print("完成 ！")
    print("输入：1 九九乘法表  输入：2 目录大小统计  输入 ：3  学生信息管理")
    number = int(input("请输入作业编号："))
    return number


if __name__ == '__main__':
    print(r"Python学习第一周作业本周共计3个作业："+"\n"
          r"1) 使用while和for…in两个循环分别输出四种九九乘法表效果（共计8个）。"+"\n"
          r"2) 使用文件和目录操作，定义一个统计指定目录大小的函数（注意目录中还有子目录）。"+"\n"
          r"3) 参考1.10的综合案例中的学生信息管理，来实现一个自动取款机的存取款模拟效果。"+"\n"
          r"要求有登陆和退出、查询余额、取钱，存钱等操作。"+"\n"
          r"学员 ：邱国昌 日期：2018-03"+"\n")
    print("※"*15)
    print("输入：1 九九乘法表  输入：2 目录大小统计  输入 ：3  学生信息管理")
    workNo = int(input("请输入作业编号："))
    if workNo == 1:
        if work1():  # 调用函数并判断是否已正常完成，如完成则嵌套调用
            workNo = commonprint()
    if workNo == 2:
        if work2():  # 调用函数并判断是否已正常完成，如完成则嵌套调用
            workNo = commonprint()
    if workNo == 3:
        if work3():  # 调用函数并判断是否已正常完成，如完成则嵌套调用
            workNo = commonprint()


