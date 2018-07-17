import pymysql
from flask_sqlalchemy import SQLAlchemy as sqlmy
from flask import Flask

app = Flask(__name__)

#这里登陆的是root用户，要填上自己的密码，MySQL的默认端口是3306，填上之前创建的数据库名test
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost:3306/webmonitor'
#设置这一项是每次请求结束后都会自动提交数据库中的变动
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True

db = sqlmy(app)

"""
主机表
"""
class Hosts(db.Model):
    __tablename__ = 'hosts'
    # id
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    # 标签
    tag = db.Column(db.String(45), unique=True,nullable=False)
    # IP地址
    ip = db.Column(db.String(45), unique=True,nullable=False)
    # cpu
    cpu = db.Column(db.String(45))
    # 内存
    mem = db.Column(db.String(45))
    # 硬盘
    hd = db.Column(db.String(45))
    # cpu = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return '<Hosts %r>' % self.tag

"""
用户表
"""
class Hosts(db.Model):
    __tablename__ = 'hosts'
    # id
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    # 用户名
    username = db.Column(db.String(45), unique=True,nullable=False)
    # 密码
    passwd = db.Column(db.String(45), nullable=False)
    # 最后登录时间
    lastlogin = db.Column(db.String(45))

    def __repr__(self):
        return '<Hosts %r>' % self.username


