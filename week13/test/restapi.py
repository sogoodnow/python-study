from flask import Flask,jsonify,request
from flask import render_template
import redis
app = Flask(__name__)

@app.route("/machine")
def getmachine():
    data = [1,2,3]
    return jsonify(data)

@app.route("/machine/create",methods=['POST'])
def getmachine():
    print(request.form)
    return jsonify({"status":False,"data":"nonono"})