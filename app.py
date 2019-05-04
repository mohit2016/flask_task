from flask import Flask, render_template,request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm


app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///site.db"

db = SQLAlchemy(app)


class Product(db.Model):
	id = db.Column(db.Integer,primary_key =True)
	title =db.Column(db.String(100),nullable =False)
	content = db.Column(db.Text,nullable =False)

	def __repr__(self):
		return f"Product('{self.title}','{self.content}')"

db.drop_all()

db.create_all()

products = [
	{
	'title' : "iPhone X",
	'content': "This is iPhone "
	},
	{
	'title' : "Macbook Pro",
	'content': "Buy Macbook"
	}
]

for product in products:
	p=Product(title=product['title'],content=product['content'])
	db.session.add(p)
	db.session.commit()





@app.route("/")
def home():
	all_products = Product.query.all() 
	return render_template('home.html', products = all_products)




@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    product = Product.query.filter_by(title=text)
    return render_template('home.html', products = product)
    

@app.route('/<name>' )
def index(name):
	p = Product.query.filter_by(id=name).first()
	mail = " "+ str(p.id)  + " " + p.title   + " "+ p.content

	import smtplib
	server = smtplib.SMTP('smtp.gmail.com', 587)

	
	server.login("youremailusername", "password")


	server.sendmail("you@gmail.com", "target@example.com", mail)



