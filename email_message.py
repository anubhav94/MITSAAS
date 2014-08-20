import smtplib
from email.MIMEText import MIMEText
import email

import SimpleHTTPServer
import SocketServer

import urlparse

PORT = 8000


def send_email(fromaddr, sub, body):
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
    print "Subject :", sub
    print "Body :", body

    msg = email.MIMEMultipart.MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = email.Utils.COMMASPACE.join(tolist)
    msg['Subject'] = sub
    msg.attach(MIMEText(body))
    msg.attach(MIMEText('\nSent from saas.mit.edu', 'plain'))
    server.sendmail(user, tolist, msg.as_string())


class ServerHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):

    def do_GET(self):
        print self.path
        if self.path == "/email_message.py":
            # This check required to make sure no one can see this file
            return
        if self.path.startswith('/contact.html?'):
            path = self.path[14:]
            params = urlparse.parse_qs(path)
            send_email(
                params['from'][0], params['subject'][0], params['message'][0])

        SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)


if __name__ == '__main__':
    Handler = ServerHandler

    httpd = SocketServer.TCPServer(("", PORT), Handler)

    print "Serving at port", PORT
    httpd.serve_forever()
