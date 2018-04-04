from django.db import models

# Create your models here.
class Stu(models.Model):
    """
    属性对应表字段
    """
    name = models.CharField(max_length=30)
    age = models.SmallIntegerField()
    sex = models.IntegerField()
    classid = models.CharField(max_length=45)

    def __str__(self):
        return  "姓名:{},年龄:{},性别:{},课程班级:{}".format(self.name,self.age,self.sex,self.classid)

    class Meta:
        db_table = "student"
