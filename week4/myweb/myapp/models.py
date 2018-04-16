from django.db import models,connection
import PIL
# Create your models here.


class Userinfo(models.Model):
    """
    学员表
    """
    name = models.CharField(max_length=30,name="name")  #姓名
    age = models.IntegerField(name="age")   #年龄
    phone = models.CharField(max_length=13,name="phone")    #电话
    sex = models.IntegerField(name="sex")   #性别
    classname = models.CharField(max_length=45,name="classname")    #课程名称
    picpath = models.ImageField(upload_to='./')
    def __str__(self):
        return "姓名：{} 年龄：{} 电话：{} 性别：{} 课程：{} 图片路径：{}".format(self.name,self.age,self.phone,self.sex,self.classname,self.picpath)
    class Meta:
        db_table = "userinfo" #数据库表名

class Pics(models.Model):
    """
    图片表
    """
    uid = models.IntegerField(name="uid")                             #学员id
    pictitle = models.CharField(max_length=45,name="pictitle")        #图片标题
    bpicname = models.CharField(max_length=45,name="bpicname")        #图片名称
    spicname = models.CharField(max_length=45,name="spicname")        #小图片名称
    updatetime = models.CharField(max_length=40,name="updatetime")    #更新时间
    def __str__(self):
        return "学员id：{} 图片标题：{} 图片名称：{} 小图片名称：{} 更新时间：{} ".format(self.uid,self.pictitle,self.bpicname,self.spicname,self.updatetime)
    class Meta:
        db_table = "pics" #数据库表名
        ordering = ['id']