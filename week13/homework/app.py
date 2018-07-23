from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from week13.homework.sqlmodels import Hosts,Users

app = Flask(__name__)



@app.route('/')
def hello_world():
    pass
    # return render_template('login.html')


if __name__ == '__main__':
    app.run()
