#!/usr/bin/env python


import sys
sys.stderr = sys.stdout
from cgi import FieldStorage

import smtplib
from email.MIMEText import MIMEText
import email

print "Content-type: text/html"
print


def send_email(fromaddr, subject, message):
    user = 'mitsaasboard'
    passw = 'ramsdick'

    smtp_host = 'smtp.gmail.com'
    smtp_port = 587
    server = smtplib.SMTP()
    server.connect(smtp_host, smtp_port)
    server.ehlo()
    server.starttls()
    server.login(user, passw)
    tolist = ['saas@mit.edu', fromaddr]

    msg = email.MIMEMultipart.MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = email.Utils.COMMASPACE.join(tolist)
    msg['Subject'] = subject
    msg.attach(MIMEText(message))
    msg.attach(MIMEText('\nSent from saas.mit.edu', 'plain'))
    server.sendmail(user, tolist, msg.as_string())

f = FieldStorage()
fromaddr = message = subject = None
if "from" in f:
    fromaddr = f["from"].value
if "message" in f:
    message = f["message"].value
if "subject" in f:
    subject = f["subject"].value

# TODO: Add more checks in here
if fromaddr and message and subject:
    # Success page
    send_email(fromaddr, subject, message)
    f = open('thank_you.html')
    print f.read()
else:
    # Rejection page
    f = open('oops.html')
    print f.read()
