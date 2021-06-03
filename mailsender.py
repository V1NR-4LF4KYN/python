import smtplib 
import ssl

#vars
sender = 'james066@gmx.de'
receiver = sender

message = """From: From Person <james066@gmx.de>
To: To Person <james066@gmx.de>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

# sending mail
try:
   smtpObj = smtplib.SMTP('localhost')
   smtpObj.sendmail(sender, receiver, message)         
   print("Successfully sent email")
except SMTPException:
   print("Error: unable to send email")
