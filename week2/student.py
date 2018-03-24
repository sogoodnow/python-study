import pymysql
import wx

# 将上周1.10的综合案例《在线学生信息管理》改成数据库操作版的。
# 1. 编写stu表信息操作类：内有方法：构造方法实现数据库连接；析构方法关闭数据连接；
# findAll( )--查询方法 、del（id）-- 删除方法   insert（data）--添加方法
# 2. 使用使用上面自定义stu表操作类，结合1.10的综合案例，做出增，删，查询操作。

class Student:


    def __init__(self, host, user, password, dbname,table):
        """
        初始化时连接数据库
        :param host:主机
        :param user:用户名
        :param password:密码
        :param dbname:数据库
        """
        self.host = host
        self.user = user
        self.password = password
        self.dbname = dbname
        self.table = table
        self.state = False
        try:
            self.connection = pymysql.connect(host = self.host,user = self.user, password = self.password, db = self.dbname,  charset = "utf8")
            self.cursor = self.connection.cursor()
            self.state = True
            print("数据库连接成功")
        except Exception as con_err:
            print("连接异常！")


    def __del__(self):
        """
        销毁对象时关闭连接
        """
        self.cursor.close()
        self.connection.close()


    def findAll(self):
        """
        :return:查询返回所有表记录
        """
        try:
            if self.cursor.execute("select * FROM %s" % self.table) > 0:
                return  self.cursor.fetchall()
            else:
                print("没有记录！")
        except Exception as all_err:
            print("连接错误：", all_err)


    def del_stu(self,stu_id):
        """
        删除特定id的学生
        :param stu_id:
        :return:
        """
        count = 0
        try:
            query_del = ("delete from student where sid=%s"%stu_id)
            count = self.cursor.execute(query_del)
            self.connection.commit()
        except Exception as del_err:
            print("删除出错:",del_err )
        return count


    def insert_stu(self, params):
        """
        插入学生记录
        :param name:姓名
        :param age: 年龄
        :param sid: 课程
        :return:
        """
        count = 0 # 成功插入条数
        try:
            query_insert = "insert into student (name,age,classid) VALUES (%s,%s,%s)" # 插入语句
            count = self.cursor.execute(query_insert,params) # 参数为列表形式
            self.connection.commit()
        except Exception as ins_err:
            print("添加出错:", ins_err)
        return count



if __name__ == '__main__':

    def search(event):
        """
        按下搜索按钮后检索所有信息
        :param event:
        :return:
        """
        stu = Student("localhost", "root", "root", "blogdb","student")
        txt_res.WriteText("========连接成功！========"+"\n")
        txt = ""
        for row in stu.findAll():
            txt += "id:{:<6}   姓名：{:<8}  年龄：{:<6}  课程：{:<10}".format(row[0],row[1],row[2],row[3])
            txt += "\n"
        txt_res.WriteText(txt)
        txt_res.WriteText("==="*3+"查询完成！"+"==="*3+"\n")
        del stu


    def del_stu(event):
        """
        删除输入的id对应记录
        :param event:
        :return:
        """
        if txt_search.GetValue():
            stu_id = txt_search.GetValue() # 获取文本框内容
            stu = Student("localhost", "root", "root", "blogdb", "student") # 实例化类，连接数据库
            if stu.del_stu(stu_id) > 0: # 找到对应学生
                txt_res.WriteText("========删除成功！========" + "\n")
            else: # 没有找到学生
                txt_res.WriteText("========没有找到该学生！========" + "\n")
        else: # 没有输入id内容时
            txt_res.WriteText("===" * 3 + "请输入id号！" + "===" * 3 + "\n")




    # ========创建应用
    app = wx.App()
    # ========创建窗口,第一个参数为父窗口
    win = wx.Frame(None,title = "学员管理系统",size=(500,450))

    # ========创建按钮
    bt_search = wx.Button(win, label="搜索全部", pos=(250, 5), size=(80, 30)) # 查询按钮，用于查询学生
    bt_add = wx.Button(win, label="添加", pos=(350, 5), size=(50, 30))
    bt_del = wx.Button(win, label="删除", pos=(420, 5), size=(50, 30))
    lab_id = wx.StaticText(win, label = u'输入删除学员ID', style=wx.ALIGN_LEFT ,size=(150, 30), pos=(10, 14))
    txt_search = wx.TextCtrl(win, pos=(140, 5), size=(100, 30))
    txt_res = wx.TextCtrl(win, pos=(20, 150), size=(440, 250), style = wx.TE_MULTILINE | wx.VSCROLL)
    # =========姓名输入
    lab_name = wx.StaticText(win, label=u'学生姓名:', style=wx.ALIGN_LEFT, size=(150, 50), pos=(10, 64))
    txt_name = wx.TextCtrl(win, pos=(140, 64), size=(100, 20) )
    # =========姓名输入
    lab_age  = wx.StaticText(win, label=u'年龄:', style=wx.ALIGN_LEFT, size=(150, 50), pos=(10,84))
    txt_age = wx.TextCtrl(win, pos=(140, 84), size=(100, 20))
    # =========班级输入
    lab_class = wx.StaticText(win, label=u'参加班级:', style=wx.ALIGN_LEFT, size=(150, 30), pos=(10, 104))
    txt_class = wx.TextCtrl(win, pos=(140, 104), size=(100, 20))

    # ========按钮事件
    bt_search.Bind(wx.EVT_BUTTON, search)
    bt_del.Bind(wx.EVT_BUTTON, del_stu)



    # ========设置可见
    win.Show()
    # ========加载主程序
    app.MainLoop()

    # 创建对象并建立连接 可以改为从文件中读取配置信息
    # try:
    #     stu = Student("localhost", "root", "root", "blogdb")
    #     print("连接成功！")
    #     params = ["张三", 26 ,"Python一期"]
    #     cout = stu.insert_stu(params)
    #     print(cout)
    # except Exception as err:
    #     print("连接错误：",err)


