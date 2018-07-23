from flask import Flask
from flask.json import jsonify
from flask_sqlalchemy import SQLAlchemy
from week13.homework.sqlmodels import Hosts,Users

app = Flask(__name__)



@app.route('/login',methods=['POST'])
def hello_world():
    return  jsonify({'status': "ok"})

@app.after_request
def after_filter(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET,POST,DELETE,PUT,'
    allow_headers = "Referer,Accept,Origin,User-Agent"
    response.headers['Access-Control-Allow-Headers'] = allow_headers

    return response
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
