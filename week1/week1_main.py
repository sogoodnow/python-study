"""
Python学习第一周作业
本周共计3个作业：
1) 使用while和for…in两个循环分别输出四种九九乘法表效果（共计8个）。
2) 使用文件和目录操作，定义一个统计指定目录大小的函数（注意目录中还有子目录）。
"""
from week1 import week1_multi99, week1_file


def common_print():
    """用于主函数执行后输出的共通信息
    return ：返回值为接收到的终端录入命令
    """
    print("完成 ！")
    print("输入：1 九九乘法表  输入：2 目录大小统计")


if __name__ == '__main__':
    print(r"Python学习第一周作业本周共计3个作业："+"\n"
          r"1) 使用while和for…in两个循环分别输出四种九九乘法表效果（共计8个）。"+"\n"
          r"2) 使用文件和目录操作，定义一个统计指定目录大小的函数（注意目录中还有子目录）。"+"\n"
          r"邱国昌 日期：2018-03"+"\n")
    print("※"*15)
    while True:
        workNo = 0
        workNo = int(input("请输入作业编号："))
        if workNo == 1:
            if week1_multi99.work1():  # 调99乘法表
                common_print()
        elif workNo == 2:
            path = input("请输入文件目录：")
            count_all = 0
            count_all = week1_file.count_size(path)
            if count_all:  # 调文件大小统计
                print("合计大小为：", count_all)
                common_print()
        else:
            print("无效输入！")
            break


