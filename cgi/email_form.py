#!/usr/bin/env python

#---------------------------------------------------------------------
# Import the necessary module.
#---------------------------------------------------------------------
import CaptchasDotNet

#---------------------------------------------------------------------
# Construct the captchas object. Replace the required parameters
# 'demo' and 'secret' with the values you receive upon
# registration at http://captchas.net.
#
# Optional Parameters and Defaults:
#
# alphabet: 'abcdefghkmnopqrstuvwxyz' (Used characters in captcha)
# We recommend alphabet without mistakable ijl.
#
# letters: '6' (Number of characters in captcha)
#
# width: '240' (image width)
# height: '80' (image height)
#
# Don't forget the same settings in check.cgi
#---------------------------------------------------------------------
captchas = CaptchasDotNet.CaptchasDotNet(
    client='mitsaaas',
    secret='b7Oi0pAbWVT76mJujsuyruGRFynXb1AGaBcxGuhk'
)

#---------------------------------------------------------------------
# Print html page
#---------------------------------------------------------------------
print 'Content-Type: text/html'
print
print '''
<html>
  <head>
    <title>Contact us!</title>
    <link rel="stylesheet" type="text/css" href="/stylesheets/index.css">
    <link rel="stylesheet" href="http://yui.yahooapis.com/pure/0.5.0/pure-min.css">
    <link rel="stylesheet" href="http://yui.yahooapis.com/pure/0.5.0/grids-responsive-min.css">
  </head>
  <body>
      <div class="contactbox">
        <div class='heading'>Keeping in Touch</div>
        <div class="content">
          Visit us on Facebook! Join <a href="https://www.facebook.com/groups/mitsaas/">our Facebook group</a> to stay updated and show your support for MIT SAAS. Email us at saas@mit.edu with any questions.
        </div>
        <form action="/cgi/email_message.py" method="get" enctype="text/plain" class ="pure-form pure-form-stacked">
          <fieldset>

            <div>
              <div style='display: inline-block'>
                <input class="contactinputbox" name='from' id="name" type="text" placeholder="Email" style="border-radius: 10px;"/>
                <input class="contactinputbox" name='subject' id="subject" type="text" placeholder="Subject" style="border-radius: 10px;"/>
                <input type="hidden" name="random" value="%s" />
                %s (<a href='/cgi/email_form.py'>New code</a>)
                <input class="contactinputbox" name='captcha' id="captcha" type="text" placeholder="Captcha text" style="border-radius: 10px;"/>
              </div>
              <br>
              <textarea class="contactinputbox" name='message' id="message" cols="83%%" rows="8" placeholder="Message" style="width: 100%%; border-radius: 10px;"></textarea>

            </div>
            <br> <br>

            <button type="submit" class="pure-button pure-button-primary" style="float: right; font-size: 24px; font-weight: 100; background: rgb(100, 6, 6); border-radius: 10px;">submit >></button>
            <br> <br> <br>
          </fieldset>
        </form>
        <footer style="margin-bottom: 20px;">
          <center>
            <br>
            &#169; MIT SAAS 2014 | saas@mit.edu
          </center>
        </footer>
      </div>
  </body>
</html>
''' % (captchas.random(), captchas.image())
#---------------------------------------------------------------------
# End
#---------------------------------------------------------------------
