from flask import Flask, request, Response
from flask_sqlalchemy import SQLAlchemy
import json


app = Flask(__name__)


app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    name = db.Column(db.String(84), nullable=False)

    def __str__(self):
        return self.name

    def __init__(self, name):
        self.name = name


@app.route("/users", methods=["GET"])
def index():
    users = User.query.all()
    return Response(json.dumps(users), status=200, mimetype="application/json")

if __name__ == '__main__':
   db.create_all()
   app.run(debug = True)