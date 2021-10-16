from enum import unique
from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)

# Add DataBase
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

# Secret Key
app.config['SECRET_KEY'] = "SOME SECRET we must change them"

#Initialize Database
db = SQLAlchemy(app)

#Create Model Data Base
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(80), nullable=False, unique=True)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    # Create A String
def __repr__(self):
    return '<Name %r>' % self.name

class UserForm(FlaskForm):
    name = StringField ("Enter Name", validators=[DataRequired()])
    email = StringField("Enter @mail", validators=[DataRequired()])
    submit = SubmitField("Submit")

@app.route('/user/add', methods=['GET', 'POST'])
def add_user():
    name = None
    form = UserForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        if user is None:
            user = Users(name=form.name.data, email=form.email.data)
            db.session.add(user)
            db.session.commit()
        name = form.name.data
        form.name.data = ''
        form.email.data = ''
        flash("User Added Successfuly!")
    our_users = Users.query.order_by(Users.date_added)
    return render_template("add_user.html", form=form, name=name, our_users=our_users)

# Create Form Class
class NamerForm(FlaskForm):
    name = StringField ("What's Your Name", validators=[DataRequired()])
    submit = SubmitField("Submit")


@app.route("/")
def index():
    #url = random.choice(images)
    return render_template("index.html")

# Create Name Page
@app.route('/name', methods=['GET', 'POST'])
def name():
    name = None
    form = NamerForm()
    # Validate Form
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        flash("Form Submitted Successfuly!")

    return render_template("name.html",
        name = name,
        form = form)


# Create Cstom Error Pages
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500
