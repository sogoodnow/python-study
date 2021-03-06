from flask import Flask,request
from flask.json import jsonify
from week13.homework.sqlmodels import  db,Machine,Monitor
from sqlalchemy import and_
from week13.homework.sqlhelper import models_to_dict
import paramiko
from week13.homework.deploy import  Deploy


app = Flask(__name__)

#这里登陆的是root用户，要填上自己的密码，MySQL的默认端口是3306，填上之前创建的数据库名test
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3306/webmonitor'
#设置这一项是每次请求结束后都会自动提交数据库中的变动
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True

db.init_app(app)

# db = sqlmy(app)

# 登录方法
@app.route('/login',methods=['POST','GET'])
def hello_world():
    # 获取表单提交数据
    username = request.form['user']
    print(username)
    passwd = request.form['passwd']
    # model = User()
    # 判断是否匹配用户名密码
    count = Machine.query.filter(and_(Machine.username== username ,Machine.passwd == passwd)).count()
    print(count)
    # 如果匹配，添加用户至session
    if count>0:
        return  jsonify({"count":count})


# 获取机器列表
@app.route('/machine',methods=['GET'])
def mahcine():
    data = Machine.query.all()
    return jsonify(models_to_dict(data))

# 删除机器
@app.route('/machine/delete',methods=['GET'])
def mahcine_delete():
    model = Machine.query.get(request.args['id'])
    db.session.delete(model)
    db.session.commit()
    return jsonify({"status":True})

# 添加机器
@app.route('/machine/create',methods=['POST'])
def mahcine_create():
    model = Machine()
    model.name = request.form['name']
    model.ip = request.form['ip']
    model.user = request.form['user']
    model.password = request.form['password']
    db.session.add(model)
    db.session.commit()
    return jsonify({"status":True})

# 机器详情
@app.route('/monitor')
def monitor():
    # 通过id获取机器ip地址
    machine = Machine.query.get(request.args['id'])
    # 通过paramiko连接远程主机并获取信息
    transport = paramiko.Transport(machine.ip,22)
    transport.connect(username=machine.user,password=machine.password)
    sftp = paramiko.SFTPClient.from_transport(transport)
    # 上传文件
    sftp.put("./monitor.py","/root/monitor.py")
    # 列出目录
    print(sftp.listdir(path='/root'))
    sftp.close()
    transport.close()
    # 执行远程文件
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    ssh.connect(hostname=machine.ip, username=machine.user, password=machine.password, port=22)
    command = "python3 /root/monitor.py "
    stdin,stdout,stderror = ssh.exec_command(command)
    err = stderror.read().decode()
    if err:
        print(err)
        ssh.close()
        return jsonify({'data':"error"})
    else:
        res = stdout.read().decode()
        ssh.close()
        return res

@app.route('/deploy',methods=['POST'])
def deploy():
    ip = request.form['ip']
    username = request.form['username']
    password = request.form['password']
    clinet = Deploy(ip,username,password,22)
    # clinet = Deploy.host()
    res = clinet.do_deploy()
    print(res)
    return jsonify({"status":True})



# 跨域处理
@app.after_request
def after_filter(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET,POST,DELETE,PUT,'
    allow_headers = "Referer,Accept,Origin,User-Agent"
    response.headers['Access-Control-Allow-Headers'] = allow_headers

    return response
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
