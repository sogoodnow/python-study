from flask import Flask,request,render_template
from flask.json import jsonify
from week13.homework.sqlmodels import  db,Hosts,User
from sqlalchemy import and_
from week13.homework.sqlhelper import models_to_dict


app = Flask(__name__)

#这里登陆的是root用户，要填上自己的密码，MySQL的默认端口是3306，填上之前创建的数据库名test
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3306/webmonitor'
#设置这一项是每次请求结束后都会自动提交数据库中的变动
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True

db.init_app(app)
# db = sqlmy(app)

@app.route('/login',methods=['POST','GET'])
def hello_world():
    # 获取表单提交数据
    username = request.form['user']
    print(username)
    passwd = request.form['passwd']
    # model = User()
    # 判断是否匹配用户名密码
    count = User.query.filter(and_(User.username== username ,User.passwd == passwd)).count()
    print(count)
    # 如果匹配，添加用户至session
    if count>0:
        return  jsonify({"count":count})

@app.after_request
def after_filter(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET,POST,DELETE,PUT,'
    allow_headers = "Referer,Accept,Origin,User-Agent"
    response.headers['Access-Control-Allow-Headers'] = allow_headers

    return response
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
