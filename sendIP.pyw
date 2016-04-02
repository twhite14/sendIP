#sendIP v1.0
#Periodically executed using Windows Task Scheduler. If the local IP address of this PC has changed since last run, email it to the specified address.
#This comes in handy when your IP is subject to change without warning.

import socket                           #To obtain local IP
import smtplib                          #To send email 
from email.mime.text import MIMEText    #To format email

#Make sure the file exists. Really only needed for first run.
try:
  lastMSG = open('last.txt', 'r')
except IOError:
  lastMSG = open('last.txt', 'w')
  lastMSG.close()
  lastMSG = open('last.txt', 'r')

#Add local IPs to a list
ipList = []
for ip in (socket.gethostbyname_ex(socket.gethostname())[2]):
  ipList.append(ip)

#Create the content of the email message. Also used in a comparison to check if a new message is required.
content = 'The Local IP address of REDACTED-PC has changed. It is now one of these:\n'
for ip in ipList:
  content = content + ip + '\n'

#Get the contents of the last message sent
lastMSGTxt = lastMSG.read()

#Compare, send message if needed. Close files.
if(lastMSGTxt != content):
  lastMSG.close()
  lastMSG = open('last.txt', 'w')
  lastMSG.write(content)
  lastMSG.close()
  
  #Define who sends and receives the mail
  gmailUsername = 'REDACTED'
  gmailPassword = 'REDACTED'
  recipient = 'REDACTED'

  #Create an email message
  msg = MIMEText(content)
  msg['Subject'] = 'New IP Address for REDACTED-PC'
  msg['From'] = gmailUsername
  msg['To'] = recipient

  #Connect to the SMTP server
  mail = smtplib.SMTP('smtp.gmail.com', 587)
  #Server handshakes
  mail.ehlo()
  mail.starttls()

  #Send the message
  mail.login(gmailUsername, gmailPassword)
  mail.sendmail(gmailUsername, recipient, msg.as_string())
  mail.quit
else:
  lastMSG.close()