import smtplib

def send_email(mailto,subject,msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        
        sender_email = 'loong.wissawakorn@gmail.com'
        sender_password = 'abc123456'
        
        server.login(sender_email,sender_password)
        
        message = 'Subject: {}\n\n{}'.format(subject,msg)
        server.sendmail(sender_email,mailto,message)
        
        server.quit()
        print('Success: Email sent')
    except:
        print('Email failed to send.')

subject = 'Hello Lungtu Krub'
msg = '''Hello Lungtu I am Uncle Engineer
I Love you Na krub. Su Su! hey! '''

send_email('Lungtu@gmail.com',subject,msg)
