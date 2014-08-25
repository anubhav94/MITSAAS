#!/usr/bin/env python


import sys
import CaptchasDotNet
sys.stderr = sys.stdout
from cgi import FieldStorage

import smtplib
from email.MIMEText import MIMEText
import email
import re

print "Content-type: text/html"
print

captchas = CaptchasDotNet.CaptchasDotNet(
    client='mitsaaas',
    secret='b7Oi0pAbWVT76mJujsuyruGRFynXb1AGaBcxGuhk'
)


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
    tolist = ['deepakn94@gmail.com', fromaddr]

    msg = email.MIMEMultipart.MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = email.Utils.COMMASPACE.join(tolist)
    msg['Subject'] = subject
    msg.attach(MIMEText(message))
    msg.attach(MIMEText('\nSent from saas.mit.edu', 'plain'))
    server.sendmail(user, tolist, msg.as_string())


def verify_email(email):
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return False
    return True

f = FieldStorage()
fromaddr = message = subject = captcha = random_string = None
error_msg = "Looks like you have a missing field or two!"
if "from" in f:
    fromaddr = f["from"].value
    if not verify_email(fromaddr):
        fromaddr = None
        error_msg = "Looks like the email you entered has a typo!"
if "message" in f:
    message = f["message"].value
if "subject" in f:
    subject = f["subject"].value
if "captcha" in f:
    captcha = f["captcha"].value
if "random" in f:
    random_string = f["random"].value

if fromaddr and message and subject:
    captchas.validate(random_string)
    if captcha and captchas.verify(captcha):
        # Success page
        send_email(fromaddr, subject, message)
        f = open('thank_you.html')
        print f.read()
    else:
        # Rejection page
        error_msg = "Oops, looks like the captcha code you entered is incorrect!"
        f = open('oops.html')
        html = f.read()
        html = html.format(error_msg)
        print html
else:
    # Rejection page
    f = open('oops.html')
    html = f.read()
    html = html.format(error_msg)
    print html
