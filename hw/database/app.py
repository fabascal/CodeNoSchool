from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy 

import os

dbdir = "sqlite:///" + os.path.abspath(os.getcwd()) + "/database.db"

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = dbdir
app.config["SQLALCHEMY_TRAK_MODIFICATIONS"] = False
db = SQLAlchemy(app)



class Posts(db.Model):
		id = db.Column(db.Integer,primary_key=True,index=True)
		title = db.Column(db.String(50))
		

@app.route("/")
def index():
	titulo="Home!"
	lista = ["footer","header","body"]
	return render_template("index.html",titulo=titulo,lista=lista)


@app.route("/insert/default")
def insert_default():
	new_post = Posts(title="Default Title")
	db.session.add(new_post)
	db.session.commit()
	return "The default post was created"

if __name__=="__main__":
	db.create_all()
	app.run(debug=True,port =9999)

