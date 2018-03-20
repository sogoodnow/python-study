# 使用文件和目录操作，定义一个统计指定目录大小的函数（注意目录中还有子目录）
# 学员姓名：邱国昌
# 日期：2018-03-15
import os


def copyfile(file1, file2):
    """
    用于文件复制
    :param file1:源文件
    :param file2: 目标文件
    :return:
    """

    #  打开文件
    f1 = open(file1, "rb")
    f2 = open(file2, "wb")
    #  读取并拷贝文件
    content = f1.readline()
    # print(content)
    while len(content) > 0:
        # print(content)
        f2.write(content)
        content = f1.readline()
    # 关闭文件流
    f1.close()
    f2.close()


def copyfolder(path1, path2):
    """
    用于简单的目录拷贝
    :param path1: 源目录
    :param path2: 目标目录
    :return:
    """
    # 获取源目录下的所有文件及文件夹列表
    file_list = os.listdir(path1)
    #  判断目标文件夹是否存在，若不存在则创建文件夹
    if not os.path.exists(path2):
        os.mkdir(path2)
    # 遍历源文件夹下的文件
    for i in file_list:
        # 判断当前文件大小是否为0，为0则为文件夹，需要递归调用函数，若为文件则复制文件
        if os.path.getsize(os.path.join(path1, i)):
            copyfile(os.path.join(path1, i), os.path.join(path2, i))
        else:
            copyfolder(os.path.join(path1, i), os.path.join(path2, i))


sum_size = 0  # 定义全局变量存储大小，初始为0
def count_size(path):
    """
    计算制定目录及子目录的大小
    :param path: 指定目录
    :return: 文件夹大小
    """
    global sum_size  # 引入全局变量
    if os.path.exists(path):  # 判断路径是否存在
        for i in os.listdir(path):  # 存在则遍历路径下文件及文件夹
            if os.path.getsize(os.path.join(path, i)):   # 计算文件大小,不为0则累加
                sum_size += os.path.getsize(os.path.join(path, i))
                print("文件名：{}，单文件大小：{},累计大小：{}".format(os.path.join(path, i),
                                                  os.path.getsize(os.path.join(path, i)),
                                                  sum_size))
            else:  # 为0则为文件夹，递归调用函数
                count_size(os.path.join(path, i))
    else:  # 为空则表示返回错误信息
        print("没有找到指定目录")
    # print("文件总大小为：", sum_size)
    return sum_size



