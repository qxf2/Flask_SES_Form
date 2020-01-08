from random import randint
from time import strftime
from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import boto3

DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'SjdnUends821Jsdlkvxh391ksdODnejdDw'


class ReusableForm(Form):
    name = TextField('Name:', validators=[validators.required()])
    email = TextField('Email:', validators=[validators.required()])


@app.route("/", methods=['GET', 'POST'])
def hello():
    form = ReusableForm(request.form)

    #print(form.errors)
    if request.method == 'POST':
        name=request.form['name']
        email=request.form['email']

        if form.validate():
            flash('Hello: {} {}'.format(name, email))
            return render_template('thank_you.html',respondent1=name,respondent2= email)
        else:
            flash('Error: All Fields are Required')

    return render_template('index.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)
