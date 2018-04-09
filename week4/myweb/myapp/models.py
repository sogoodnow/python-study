from django.db import models

# Create your models here.


class Userinfo(models.Model):
    name = models.CharField(max_length=30,name="name")  #姓名
    age = models.IntegerField(name="age")   #年龄
    phone = models.CharField(max_length=13,name="phone")    #电话
    sex = models.IntegerField(name="sex")   #性别
    classname = models.CharField(max_length=45,name="classname")    #课程名称
    picpath = models.CharField(max_length=45,name = "picpath")  #图片存放路径

    def __str__(self):
        return "姓名：{} 年龄：{} 电话：{} 性别：{} 课程：{} 图片路径：{}".format(self.name,self.age,self.phone,self.sex,self.classname,self.picpath)
    class Meta:
        db_table = "userinfo" #数据库表名