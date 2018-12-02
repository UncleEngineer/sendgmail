
#########################################




import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import config
'''
config.py

USER = 'yourmail@gmail.com'
PASS = '123345678'


'''
def sendthai(sendto):

	me = config.USER
	you = sendto


	# Create message container - the correct MIME type is multipart/alternative.

	msg = MIMEMultipart('alternative')
	msg['Subject'] = "TEST"
	msg['From'] = me
	msg['To'] = you

	# Create the body of the message (a plain-text and an HTML version).

	text = "สวัสดี!\nคุณสบายดีไหม?\n"

	html = """\

	<html>

	  <head></head>

	  <body>

	    <p>สวัสดีครับ!<br>

	       คุณสบายดีไหม?<br>

	    </p>

	  </body>

	</html>

	"""

	# Record the MIME types of both parts - text/plain and text/html.

	part1 = MIMEText(text, 'plain') #ส่งแบบ text
	#part2 = MIMEText(html, 'html') # ส่งแบบ html
	msg.attach(part1)

	#msg.attach(part2)


	s = smtplib.SMTP('smtp.gmail.com:587')
	s.ehlo()
	s.starttls()
	s.login(config.USER, config.PASS)
	s.sendmail(me, you.split(','), msg.as_string())

	#s.sendmail(sender, recipients.split(','), msg.as_string())

	s.quit()



sendthai('loong.wissawakorn@gmail.com')
