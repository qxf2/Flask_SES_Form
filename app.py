from random import randint
from time import strftime
from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import boto3

DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'SjdnUends821Jsdlkvxh391ksdODnejdDw'

# Amazon Web Services credentials
AWS_ACCESS_KEY_ID = 'AKIAJTAYZP5CWD5F3H4A'
AWS_SECRET_ACCESS_KEY = 'RndLBrjyRTXJ5Oo39ruMbgsWIWO4c2FX/SMKI7tt'

# Amazon Simple Email Service
SES_REGION_NAME = 'ap-south-1'  # change to match your region
SES_EMAIL_SOURCE = 'nilaya.indurkar@gmail.com'

class ReusableForm(Form):
    name = TextField('Name:', validators=[validators.required()])


def get_time():
    time = strftime("%Y-%m-%dT%H:%M")
    return time

def send_email(app, recipients, sender=None, subject='', text='', html=''):
    ses = boto3.client(
        'ses',
        region_name=app.config['SES_REGION_NAME'],
        aws_access_key_id=app.config['AWS_ACCESS_KEY_ID'],
        aws_secret_access_key=app.config['AWS_SECRET_ACCESS_KEY']
    )
    if not sender:
        sender = app.config['SES_EMAIL_SOURCE']

    ses.send_email(
        Source=sender,
        Destination={'ToAddresses': recipients},
        Message={
            'Subject': {'Data': subject},
            'Body': {
                'Text': {'Data': text},
                'Html': {'Data': html}
            }
        }
    )


@app.route("/", methods=['GET', 'POST'])
def hello():
    form = ReusableForm(request.form)

    #print(form.errors)
    if request.method == 'POST':
        name = request.form['name']
        email= request.form['email']

        if form.validate():
            flash('Hello: {} {}'.format(name))

        else:
            flash('Error: All Fields are Required')

    return render_template('index.html', form=form)

if __name__ == "__main__":
    app.run()
