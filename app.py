from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__)
app.config['SECRET_KEY'] = "SOME SECRET we must change them"

# Create Form Class
class NamerForm(FlaskForm):
    name = StringField ("What's Your Name", validators=[DataRequired()])
    submit = SubmitField("Submit")
@app.route("/")

def index():
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


# Create CUstom Error Pages
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404 

@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500
