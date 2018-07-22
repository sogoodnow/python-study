from flask import Flask, request, jsonify
from flask import render_template

import redis
app = Flask(__name__)
redis = redis.Redis(host='redis',port=6379)

@app.route('/')
def hello_world():
    count = redis.incr('hints')
    # return 'Hello World!{}'.format(count)
    return render_template()


@app.route("/machine")
def getmachine():
    data = [1, 2, 3]
    return jsonify(data)


@app.route("/machine/create", methods=['POST'])
def createmachine():
    print(request.form)
    pass


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)
