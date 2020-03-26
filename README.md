Automating Email to Verified Users with Flask and Amazon SES.
=============================================================

Sending Emails to Verified Email Ids with Flask Application using Amazon SES account.

The way to build:
================

Please refer to Blog: https://qxf2.com/blog/?p=12064&preview=true

How to use this project?
========================
1. Register to Amazon SES account. Verify Email with SES. Note down these AWS credemtials to connect to Amazon SES.

   - SES_REGION=us-east-1
   - SES_EMAIL_SOURCE=your_email
   - AWS_ACCESS_KEY_ID=your_access_key_id
   - AWS_SECRET_ACCESS_KEY=your_secret_access_key

2. Fork or Clone this repository.

3. Create Virtual Enviornment, and activate the same.

4. On virtual enviornment,with "aws.cmd configure" command configure above AWS credentials. With this you are connected to Amazon SES.

5. On your local repository, run "python app.py".

6. On Browser, open http://127.0.0.1:5000/ to view app.
