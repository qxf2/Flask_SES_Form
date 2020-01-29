Automating Email to Verified Users with Flask and Amzon SES.
===================================================

Sending Emails to Verified Email Ids with Flask Application using Amazon SES account.

The way to build this:
======================

Please refer to blog:

How to use this project?
========================
1. Register to Amazon SES account. Verify Email with SES. Update the following variables in Code.

   - SES_REGION=us-east-1
   - SES_EMAIL_SOURCE=your_email
   - AWS_ACCESS_KEY_ID=your_access_key_id
   - AWS_SECRET_ACCESS_KEY=your_secret_access_key

2. Fork or Clone this repository.

3. Update the conf file with AWS configuration.

4. On your local repository, run "python app.py".

5. On Browser, open http://127.0.0.1:5000/ to view app.
