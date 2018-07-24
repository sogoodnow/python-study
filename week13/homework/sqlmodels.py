from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
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
class User(db.Model):
    __tablename__ = 'user'
    # id
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    # 用户名
    username = db.Column(db.String(45), unique=True,nullable=False)
    # 密码
    passwd = db.Column(db.String(45), nullable=False)
    # 最后登录时间
    lastlogin = db.Column(db.String(45))

    def __repr__(self):
        return '<User %r>' % self.username


