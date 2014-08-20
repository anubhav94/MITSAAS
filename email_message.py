import smtplib
from email.MIMEText import MIMEText
import email

import SimpleHTTPServer
import SocketServer

import urlparse

PORT = 8000


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

    print "From address :", fromaddr
    print "Subject :", subject
    print "Message :", message

    msg = email.MIMEMultipart.MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = email.Utils.COMMASPACE.join(tolist)
    msg['Subject'] = subject
    msg.attach(MIMEText(message))
    msg.attach(MIMEText('\nSent from saas.mit.edu', 'plain'))
    server.sendmail(user, tolist, msg.as_string())


class ServerHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):

    def do_GET(self):
        print self.path
        if self.path.startswith('/email_message.py'):
            # This check required to make sure no one can see this file
            return
        if self.path.startswith('/contact.html?'):
            path = self.path[14:]
            params = urlparse.parse_qs(path)
            fromaddr = params.get('from', None)
            subject = params.get('subject', None)
            message = params.get('message', None)
            if fromaddr and subject and message:
                # Number of each of these parameters should only be 1
                fromaddr = fromaddr[0]
                subject = subject[0]
                message = message[0]
                send_email(fromaddr, subject, message)

        SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)


if __name__ == '__main__':
    Handler = ServerHandler

    httpd = SocketServer.TCPServer(("", PORT), Handler)

    print "Serving at port", PORT
    httpd.serve_forever()
