from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from flask_bootstrap import Bootstrap
import boto3
from conf import aws_conf as conf

DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = conf.SECRET_KEY

Bootstrap(app)

#Reusbale Form to enter name and email
class ReusableForm(Form):
    name = TextField('Name:', validators=[validators.required()])
    email = TextField('Email:', validators=[validators.required()])

#Form Main Page
@app.route("/", methods=['GET', 'POST'])
def hello():
    form = ReusableForm(request.form)
#Send email using SES resource
    ses_client = boto3.client('ses',region_name=conf.AWS_REGION)

    if request.method == 'POST':
        name=request.form['name']
        email=request.form['email']

        user_json = {}
        user_json['customer_email'] = request.form.get('email')
        user_json['comments'] = request.form.get('Thank you for your email')

        SUBJECT = 'You have a new mail'
        BODY_HTML = render_template( 'pretty_json.html', user_json = user_json )

        # sending email with all details with amzon ses
        response = ses_client.send_email(
         Destination = { 'ToAddresses': [ email, ], },
         Message={ 'Body': { 'Html': { 'Charset': conf.CHARSET, 'Data': BODY_HTML, },
                            'Text': { 'Charset': conf.CHARSET, 'Data':conf.BODY_TEXT, }, }, 
                  'Subject': { 'Charset': conf.CHARSET, 'Data': SUBJECT, },}, 
         Source=conf.SENDER, )
    
        if form.validate():
            flash('Hello: {} {}'.format(name, email))
            return render_template('thank_you.html',respondent1=name,respondent2= email)
        else:
            flash('Error: All Fields are Required')

    return render_template('index.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)
